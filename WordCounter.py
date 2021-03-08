import os
import glob


def validateHostVolume():
    # if user mounts a volume to /home/data , it should be created by alpine
    if(os.path.exists("home/data")):
        # Now create home/output to store the result.txt file
        if not os.path.exists("home/output/"):
            os.makedirs("home/output/")
        return True
    else:
        # User did not mount any directory, exit the program
        import sys
        correctDockerCommand = "\nCommand should like: \ndocker run -v your/system/directory:/home/data REPOSITORY_NAME"
        errMsg = "No Directory seems to be mounted, exiting ..."
        sys.exit(errMsg + correctDockerCommand)


def getWordCount(fileName):
    file = open(fileName, "r")
    data = file.read()
    words = data.split()
    return len(words)


def getAllTheTextFilesData():
    all_text_files = glob.glob("*.txt")
    if len(all_text_files) == 0:
        import sys
        errMsg = "No text files exist in the mounted directory\n"
        sys.exit(errMsg+"exiting ...")
    else:
        outputFile.write("\nList of text files inside(/home/data)"+"\n")
        for fileName in all_text_files:
            outputFile.write(fileName+"\n")
        return all_text_files


def getWordCountOfFiles():
    word_count_of_files = []
    for file in all_text_files:
        wordCount = getWordCount(file)
        word_count_of_files.append(wordCount)
    return word_count_of_files


def findFileWithMaxWords():
    index = word_count_of_files.index(
        max(word_count_of_files))
    return all_text_files[index]


def findIPAddrofMachine():
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr


def printOutputToConsole():
    # Close the outputFile Handler
    outputFile.close()
    # Change the dir back to normal
    os.chdir(myOriginalRootDir)
    file = open("home/output/result.txt", "r")
    print(file.read())


if __name__ == "__main__":

    # Check if our user mounted the container with required text files
    validateHostVolume()

    # Preserve the root dir
    myOriginalRootDir = os.getcwd()

    # Open result file to write all the output
    outputFile = open("home/output/result.txt", "w+")
    os.chdir("home/data/")

    # a) List name of all the text file at location: /home/data
    all_text_files = getAllTheTextFilesData()

    # b) Read text file and count total number of words in each text file
    word_count_of_files = getWordCountOfFiles()

    # c) Add all the number of words to find the grand total (total number of words in all files)
    grand_total_of_words = sum(word_count_of_files)
    outputFile.write(
        "\nTotal Number of words in all the text files:\n"+str(grand_total_of_words)+"\n")

    # d) List the file name with maximum number of words.
    fileWithMaxWords = findFileWithMaxWords()
    outputFile.write(
        "\nFile with max word count is:\n" + fileWithMaxWords+"\n")

    # e) Find the IP address of your machine
    IPAddr = findIPAddrofMachine()
    outputFile.write("\nIP address of your machine:\n" + IPAddr)

    # f) Write all the output to a text file at location: /home/output/result.txt (inside your container)
    printOutputToConsole()
