def left_join(hashmap1, hashmap2):
    '''
     function that LEFT JOINs two hashmaps into a single data structure:
         input1 ---> hashmap1
         input2 ---> hashmap2
         output >>> list of lists contain each key with values..
     '''

    output = []

    for key in hashmap1:

        output.append([key,hashmap1[key],hashmap2[key] if key in hashmap2 else None])
    return output




if __name__ == '__main__':
    hash1 = {'diligent':'employed', 'fond':'enamored', 'guide':'usher', 'outfit':'garb','wrath':'anger'}
    hash2 = {'diligent':'idle', 'fond':'averse', 'guide':'follow', 'flow':'jam','wrath':'delight'}
    print(left_join(hash1, hash2))


