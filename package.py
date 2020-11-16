def package(chars, flag:str): #puts chars from .dedupe into final, usable json for javascript
    import json
    #debugger below is strictly for the chars in the string that print backwards
    # debug_str = ""
    file_var = 'cipher.json'
    reverseDictBool = False

    def zip(file_var:str, reverseDictBool:bool):
        with open(file_var, 'w') as output:
            packaged = {}
            for k,v in enumerate(chars):
                # debug_str += v
                if reverseDictBool == False:
                    pdict = {k:v}
                else:
                    pdict = {v:k}
                packaged.update(pdict)
            json.dump(packaged, output)


    if type(chars) == str and flag == 'to_cipher':
        overwritesChars = []
        for i in chars:
            overwritesChars.append(i)
        chars = overwritesChars

    elif type(chars) == str and flag == 'to_uncipher':
        file_var = 'uncipher.json'
        reverseDictBool = True
    
    zip(file_var,reverseDictBool)
    

        #this here below is what goes into 4_debug.py after the offending chars are forcibly evicted
    # with open('cipher.txt', 'w') as output:  #### these were for the buggy chars
    #     output.write(debug_str)