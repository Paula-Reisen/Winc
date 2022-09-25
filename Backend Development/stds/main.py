# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Your code here
import sys
def main():
    # TODO: read text from stdin
    newText = sys.stdin.read()
    len_newText = len(newText)
        
    # TODO: Filter character given as an argument from the text
    arg = sys.argv[1]
    len_newText = len(newText)

    filtered_txt = newText.replace(arg, "")
    removed_chars = len_newText - len(filtered_txt)


    # TODO: Print the result to stdout

    sys.stdout.write(filtered_txt)
    # TODO: Print the total number of removed characters to stderr

    sys.stderr.write(str(removed_chars))


if __name__ == "__main__":
    main()
