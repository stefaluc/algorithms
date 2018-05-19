type Input struct {
    Text string `json:"text"`
}

type Output struct {
    W string `json:"w"`
    N int `json:"n"`
}

// GetSortedWordCount takes in a JSON-formatted byte slice of words of the form
// {"text": "text text text"}. It then lowercases each word, counts the occurrences 
// of each word, and outputs a corresponding lexicographically JSON-formatted byte 
// slice of the form [{"w": "text", "n": 3}] 
func GetSortedWordCount(inputJson []byte) ([]byte, error) {
    // parse input data from json to array of strings
    var data Input
    if err := json.Unmarshal(inputJson, &data); err != nil {
        return nil, err
    }
    strs := strings.Split(data.Text, " ")
    for i, str := range strs {
        strs[i] = strings.ToLower(str)
    }

    // calculate occurrences of each word
    wordCounts := make(map[string]int)
    for _, str := range strs {
        wordCounts[strings.ToLower(str)] = wordCounts[strings.ToLower(str)] + 1
    }

    // keep iteration order of map so it can be lexicographically sorted
    var keys []string
    for k := range wordCounts {
        keys = append(keys, k)
    }
    sort.Strings(keys)

    // convert map to expected output format struct
    var outputList []*Output
    for _, word := range keys {
        outputList = append(outputList, &Output{
            W: word,
            N: wordCounts[word],
        })
    }

    // convert struct to json
    outputListJson, err := json.Marshal(outputList);
    if err != nil {
        return nil, err
    }
    return outputListJson, nil
}
