#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

Place_Holder="[name]"

with open("Input/Letters\starting_letters.txt","r") as data_letter:
    letter_content=data_letter.read()
    #print(letter_content)

with open("Input/Names/invited_names.txt","r") as data1:
    names=data1.readlines()
    #print(names)

    for name in names:
        new_name=name.strip()
        #print(new_name)
        letter_content.replace("Angela","Thrinadh")
        new_letter=letter_content.replace(Place_Holder,new_name)
        #new_letter=letter_content.replace("Angela","Thrinadh")
        with open(f"Output/ReadyToSend/letter_to_{new_name}.txt",mode="w") as completed_letters:
            completed_letters.write(new_letter)

with open("Output/ReadyToSend/letter_to_Sokka.txt") as completed_data:
    print(completed_data.read())

# Modes have to be set correctly to work with files.







