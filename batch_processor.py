#!/usr/bin/env python3
"""
Batch Processor for One Piece Character Classifier
Processes multiple images and generates detailed reports
"""

import os
import json
import argparse
import pandas as pd
from datetime import datetime
from pathlib import Path
from PIL import Image
import torch
from model import model, transform, device, predict, dataset

class BatchProcessor:
    def __init__(self, model_path=None):
        """Initialize the batch processor"""
        self.model = model
        self.transform = transform
        self.device = device
        self.class_names = dataset.data.classes
        
        # Character data for reports
        self.character_data = {
            'Luffy': {'name': 'Monkey D. Luffy', 'crew': 'Straw Hat Pirates'},
            'Zoro': {'name': 'Roronoa Zoro', 'crew': 'Straw Hat Pirates'},
            'Nami': {'name': 'Nami', 'crew': 'Straw Hat Pirates'},
            'Usopp': {'name': 'Usopp', 'crew': 'Straw Hat Pirates'},
            'Sanji': {'name': 'Vinsmoke Sanji', 'crew': 'Straw Hat Pirates'},
            'Chopper': {'name': 'Tony Tony Chopper', 'crew': 'Straw Hat Pirates'},
            'Robin': {'name': 'Nico Robin', 'crew': 'Straw Hat Pirates'},
            'Franky': {'name': 'Franky', 'crew': 'Straw Hat Pirates'},
            'Brook': {'name': 'Brook', 'crew': 'Straw Hat Pirates'},
            'Jinbe': {'name': 'Jinbe', 'crew': 'Straw Hat Pirates'},
            'Shanks': {'name': 'Red-Haired Shanks', 'crew': 'Red Hair Pirates'},
            'Ace': {'name': 'Portgas D. Ace', 'crew': 'Whitebeard Pirates'},
            'Law': {'name': 'Trafalgar Law', 'crew': 'Heart Pirates'},
            'Kid': {'name': 'Eustass Kid', 'crew': 'Kid Pirates'},
            'Dragon': {'name': 'Monkey D. Dragon', 'crew': 'Revolutionary Army'},
            'Whitebeard': {'name': 'Edward Newgate', 'crew': 'Whitebeard Pirates'},
            'Roger': {'name': 'Gol D. Roger', 'crew': 'Roger Pirates'}
        }
    
    def process_image(self, image_path):
        """Process a single image and return prediction results"""
        try:
            # Load and preprocess image
            image = Image.open(image_path).convert("RGB")
            transformed_image = self.transform(image).unsqueeze(0).to(self.device)
            
            # Get prediction
            probabilities = predict(self.model, transformed_image, self.device)
            predicted_class = self.class_names[probabilities.argmax()]
            confidence = float(probabilities.max())
            
            return {
                'image_path': str(image_path),
                'predicted_class': predicted_class,
                'confidence': confidence,
                'probabilities': probabilities.tolist(),
                'success': True
            }
        except Exception as e:
            return {
                'image_path': str(image_path),
                'error': str(e),
                'success': False
            }
    
    def process_directory(self, input_dir, output_dir=None, file_extensions=None):
        """Process all images in a directory"""
        if file_extensions is None:
            file_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
        
        input_path = Path(input_dir)
        if not input_path.exists():
            raise ValueError(f"Input directory {input_dir} does not exist")
        
        # Find all image files
        image_files = []
        for ext in file_extensions:
            image_files.extend(input_path.glob(f"*{ext}"))
            image_files.extend(input_path.glob(f"*{ext.upper()}"))
        
        print(f"Found {len(image_files)} images to process")
        
        # Process each image
        results = []
        for i, image_file in enumerate(image_files, 1):
            print(f"Processing {i}/{len(image_files)}: {image_file.name}")
            result = self.process_image(image_file)
            results.append(result)
        
        return results
    
    def generate_report(self, results, output_dir=None):
        """Generate detailed report from batch processing results"""
        if output_dir is None:
            output_dir = Path("batch_reports")
        
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Filter successful results
        successful_results = [r for r in results if r['success']]
        failed_results = [r for r in results if not r['success']]
        
        # Create summary statistics
        summary = {
            'total_images': len(results),
            'successful_predictions': len(successful_results),
            'failed_predictions': len(failed_results),
            'success_rate': len(successful_results) / len(results) if results else 0,
            'timestamp': timestamp
        }
        
        # Character distribution
        character_counts = {}
        confidence_scores = []
        
        for result in successful_results:
            char = result['predicted_class']
            character_counts[char] = character_counts.get(char, 0) + 1
            confidence_scores.append(result['confidence'])
        
        summary['character_distribution'] = character_counts
        summary['average_confidence'] = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0
        summary['min_confidence'] = min(confidence_scores) if confidence_scores else 0
        summary['max_confidence'] = max(confidence_scores) if confidence_scores else 0
        
        # Create detailed results DataFrame
        df_results = []
        for result in results:
            row = {
                'image_path': result['image_path'],
                'success': result['success']
            }
            
            if result['success']:
                row.update({
                    'predicted_class': result['predicted_class'],
                    'confidence': result['confidence'],
                    'character_name': self.character_data.get(result['predicted_class'], {}).get('name', result['predicted_class']),
                    'crew': self.character_data.get(result['predicted_class'], {}).get('crew', 'Unknown')
                })
            else:
                row.update({
                    'error': result['error'],
                    'predicted_class': None,
                    'confidence': None,
                    'character_name': None,
                    'crew': None
                })
            
            df_results.append(row)
        
        df = pd.DataFrame(df_results)
        
        # Save reports
        # 1. Summary JSON
        summary_file = output_path / f"summary_{timestamp}.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        # 2. Detailed CSV
        csv_file = output_path / f"detailed_results_{timestamp}.csv"
        df.to_csv(csv_file, index=False)
        
        # 3. HTML Report
        html_file = output_path / f"report_{timestamp}.html"
        self._generate_html_report(summary, df, html_file)
        
        # 4. Text Report
        txt_file = output_path / f"report_{timestamp}.txt"
        self._generate_text_report(summary, df, txt_file)
        
        print(f"\nBatch processing completed!")
        print(f"Total images: {summary['total_images']}")
        print(f"Successful predictions: {summary['successful_predictions']}")
        print(f"Success rate: {summary['success_rate']:.2%}")
        print(f"Average confidence: {summary['average_confidence']:.2%}")
        print(f"\nReports saved to: {output_path}")
        print(f"- Summary: {summary_file}")
        print(f"- Detailed CSV: {csv_file}")
        print(f"- HTML Report: {html_file}")
        print(f"- Text Report: {txt_file}")
        
        return summary, df
    
    def _generate_html_report(self, summary, df, output_file):
        """Generate HTML report"""
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>One Piece Classifier - Batch Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 10px; }}
                .summary {{ background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0; }}
                .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }}
                .stat-card {{ background: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
                table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
                th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
                th {{ background: #f8f9fa; }}
                .success {{ color: #28a745; }}
                .error {{ color: #dc3545; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>One Piece Character Classifier - Batch Report</h1>
                <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            
            <div class="summary">
                <h2>Summary</h2>
                <div class="stats">
                    <div class="stat-card">
                        <h3>Total Images</h3>
                        <p>{summary['total_images']}</p>
                    </div>
                    <div class="stat-card">
                        <h3>Successful Predictions</h3>
                        <p>{summary['successful_predictions']}</p>
                    </div>
                    <div class="stat-card">
                        <h3>Success Rate</h3>
                        <p>{summary['success_rate']:.2%}</p>
                    </div>
                    <div class="stat-card">
                        <h3>Average Confidence</h3>
                        <p>{summary['average_confidence']:.2%}</p>
                    </div>
                </div>
            </div>
            
            <h2>Character Distribution</h2>
            <table>
                <tr><th>Character</th><th>Count</th><th>Percentage</th></tr>
        """
        
        for char, count in summary['character_distribution'].items():
            percentage = count / summary['successful_predictions'] * 100
            html_content += f"<tr><td>{char}</td><td>{count}</td><td>{percentage:.1f}%</td></tr>"
        
        html_content += """
            </table>
            
            <h2>Detailed Results</h2>
            <table>
                <tr>
                    <th>Image Path</th>
                    <th>Status</th>
                    <th>Predicted Character</th>
                    <th>Confidence</th>
                    <th>Crew</th>
                </tr>
        """
        
        for _, row in df.iterrows():
            status_class = "success" if row['success'] else "error"
            status_text = "Success" if row['success'] else "Failed"
            predicted = row['predicted_class'] if row['success'] else "N/A"
            confidence = f"{row['confidence']:.2%}" if row['success'] else "N/A"
            crew = row['crew'] if row['success'] else "N/A"
            
            html_content += f"""
                <tr>
                    <td>{row['image_path']}</td>
                    <td class="{status_class}">{status_text}</td>
                    <td>{predicted}</td>
                    <td>{confidence}</td>
                    <td>{crew}</td>
                </tr>
            """
        
        html_content += """
            </table>
        </body>
        </html>
        """
        
        with open(output_file, 'w') as f:
            f.write(html_content)
    
    def _generate_text_report(self, summary, df, output_file):
        """Generate text report"""
        with open(output_file, 'w') as f:
            f.write("One Piece Character Classifier - Batch Report\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("SUMMARY\n")
            f.write("-" * 20 + "\n")
            f.write(f"Total images: {summary['total_images']}\n")
            f.write(f"Successful predictions: {summary['successful_predictions']}\n")
            f.write(f"Failed predictions: {summary['failed_predictions']}\n")
            f.write(f"Success rate: {summary['success_rate']:.2%}\n")
            f.write(f"Average confidence: {summary['average_confidence']:.2%}\n")
            f.write(f"Min confidence: {summary['min_confidence']:.2%}\n")
            f.write(f"Max confidence: {summary['max_confidence']:.2%}\n\n")
            
            f.write("CHARACTER DISTRIBUTION\n")
            f.write("-" * 25 + "\n")
            for char, count in summary['character_distribution'].items():
                percentage = count / summary['successful_predictions'] * 100
                f.write(f"{char}: {count} ({percentage:.1f}%)\n")
            f.write("\n")
            
            f.write("DETAILED RESULTS\n")
            f.write("-" * 17 + "\n")
            for _, row in df.iterrows():
                f.write(f"Image: {row['image_path']}\n")
                f.write(f"Status: {'Success' if row['success'] else 'Failed'}\n")
                if row['success']:
                    f.write(f"Predicted: {row['predicted_class']}\n")
                    f.write(f"Confidence: {row['confidence']:.2%}\n")
                    f.write(f"Crew: {row['crew']}\n")
                else:
                    f.write(f"Error: {row['error']}\n")
                f.write("-" * 30 + "\n")

def main():
    parser = argparse.ArgumentParser(description='Batch process images for One Piece character classification')
    parser.add_argument('input_dir', help='Directory containing images to process')
    parser.add_argument('--output-dir', help='Output directory for reports (default: batch_reports)')
    parser.add_argument('--extensions', nargs='+', default=['.jpg', '.jpeg', '.png', '.bmp', '.tiff'],
                       help='File extensions to process')
    
    args = parser.parse_args()
    
    # Initialize processor
    processor = BatchProcessor()
    
    try:
        # Process images
        results = processor.process_directory(args.input_dir, file_extensions=args.extensions)
        
        # Generate reports
        summary, df = processor.generate_report(results, args.output_dir)
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 