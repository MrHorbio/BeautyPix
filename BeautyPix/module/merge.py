import argparse

def merge_files(file1, file2, output_file):
    # Create a set to store unique lines
    unique_lines = set()

    # Read lines from the first file and add to the set
    with open(file1, 'r') as f1:
        for line in f1:
            unique_lines.add(line.strip())

    # Read lines from the second file and add to the set
    with open(file2, 'r') as f2:
        for line in f2:
            unique_lines.add(line.strip())

    # Write the unique lines to the output file
    with open(output_file, 'w') as out_file:
        for line in unique_lines:
            out_file.write(line + '\n')

    print(f"Merged content written to {output_file} with duplicates removed.")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Merge two files and remove duplicates.")
    parser.add_argument('command', choices=['merge'], help="Command to execute (merge)")
    parser.add_argument('-f', '--files', nargs=2, required=True, help="Input files to merge")
    parser.add_argument('-o', '--output', required=True, help="Output file for merged content")

    # Parse arguments
    args = parser.parse_args()

    # Execute merge command
    if args.command == 'merge':
        file1, file2 = args.files
        output_file = args.output
        merge_files(file1, file2, output_file)

if __name__ == "__main__":
    main()
