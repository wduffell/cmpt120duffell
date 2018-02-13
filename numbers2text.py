# numbers2text

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    # Get the message to decode
    inString = input ("Please enter the Unicode-encoded message")

    # Loop through each substring and build the Unicode message
    message = ""
    for numStr in inString.split():
        # convert the string to a number
        codeNum = int(numStr)
        # append character to message
        message = message + chr(codeNum)

    print("\nThe decoded message is:", message)

main()
