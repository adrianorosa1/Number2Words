# Follow the instructions below to run the programme
1. Download the whole package as a .zip file (green button "code" in top right, then "Download Zip")
2. From the .zip file, extract the number2words.txt and num2words.ipynb to your Desktop
3. You can modify the input by modifying the number2words.txt file
4. A valid number is not separated by commas or dots, it must be an integer with no special characters 
   and it has at least one white space before and after. The input is valid if the string contains only one valid number.
5. Open the num2words.ipynb on a Jupiter notebook. Run the code and you will be asked to input the name of the .txt file that sits on your Desktop. 
   The name to input is "number2words" unless the user changed it manually after the download 
6. You will get an error with message "number invalid" in case the .txt file does not contain a valid number.
   In that case you can change the input string in the .txt file and run the programme again

# Explanation
The code consists of 3 blocks: input, error handling, conversion into words
1. Input:
   - I allowed the user to use any .txt file that sits on the Desktop, but I provided one .txt file for completion (number2words.txt). I think it is a better way to allow the user to have his/her own inputs
   - If the user inputs the wrong name (e.g. a file that does not exist), the error shown will say that the file doesn't exist. I decided not to override this error as it is self explanatory even for someone not accustomed with Python

2. Error handling:
   - I started by defining what a valid input is. The routine I had in mind was the following: a valid input has a space before and after (except if it is at the beginning or at the end of the string), it does not have any commas or dots and it is the only digits within the whole string. Hence I divided the routine into 2 checks, first to check if there is any valid number (as in with a space before and after, correcting also in case the number sits at the beginning or at the end of the string), then checking whether there was only one number. If both conditions were met, the number is valid and will enter the last function to be converted into words, otherwise an error "number invalid" will appear.

3. Conversion into words:
   - This routine is divided into 2 functions. The main function (num2words) has a while loop which divides the number into groups of 3 (hundreds, tens and units/ones), which then runs the other function (num999), that splits the group of 3 into "a", "b" and "c", where "a" is the hundreds digit, "b" is the tens digit and "c" is the units digit. The function indexes the digit into the correct location within the pre-specified lists of units and twelves (which contains enough string to get to novemtrigintillion = 10^120). The loop in the original num2words function adds the "thousand" or "million" and so on depending on how many iterations of groups of 3 there are.
   In order to have a proper formatting in the final output, several conditions have been used, depending on which iteration of the loop it is and depending on whether any or all digits of the group of 3 was equal to 0.
