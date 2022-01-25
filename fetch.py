import requests, json, os
from block import Block
from block import Question


#getting the key from the environment variables.
TOKEN = os.getenv('NOTION_KEY')

#setting the headers for the HTTPS request
headers = {
    "Authorization": "Bearer " + TOKEN,
    "Notion-Version":"2021-08-16"
}

#make sure filename is in single quotes
def dumpDataInFile(filename, data):
    with open(filename, 'w', encoding = 'utf8') as file:
        json.dump(data, file, ensure_ascii = False)

#a function for getting all the pages required - ie from the main page place
def getPageIDs(page_id, file_dump_name):
    readURL = f"https://api.notion.com/v1/blocks/{page_id}/children"
    results = requests.request("GET", readURL, headers = headers).json()

    page_ids = []
    page_titles = []

    for result in results['results']:
        #parse the JSON
        try:
            page_ids.append(result['id'])
            page_titles.append(result['child_page']['title'])
        except IndexError:
            print("Page has no children, or does not exist")
    #dumpDataInFile(f'./{file_dump_name}.json', results)
    return page_ids, page_titles

#a function for getting the blocks from a specific page ID, the base function to be called on each page
def getBlocks(page_id, current_topic):
    readURL = f"https://api.notion.com/v1/blocks/{page_id}/children"
    results = requests.request("GET", readURL, headers=headers)

    #a list for the toggle blocks, that will be the base questions in a topic file.
    toggle_blocks = []
    data = results.json()

    for result in data['results']:
        #tries to create a new block object instance but will crash if the block is empty.
        try:
            new_block = defineBlock(result, current_topic)
        except:
            continue
        #if the new block is a toggle block return it to the main function.
        if (new_block.block_type == 'toggle'):
            toggle_blocks.append(new_block)

    return toggle_blocks

#COULD IMPLEMENT RECURSION HERE, TO GET ALL THE BLOCKS
def getBlockChildren(block, current_topic):
    readURL = f"https://api.notion.com/v1/blocks/{block.block_id}/children"
    results = requests.request("GET", readURL, headers=headers)
    try:
        data = results.json()
    except:
        print("\n\nError with " + block)
    dumpDataInFile("./db3.json", data)
    blocks = []

    for result in data['results']:
        new_block = defineBlock(result, current_topic)
        blocks.append(new_block)
    return blocks

def emptyBlock(): #a form of error catching so that the blocks that aren't questions can be recognised as an empty block
    return Block("","",False,"","",False)

def defineBlock(json_result, current_topic):
    type = json_result['type']
    if type == 'image':
        try:
            return Block(json_result['id'], type, json_result['has_children'], json_result[type]['file']['url'], current_topic, True) #sets to True as image will always be answer
        except:
            return emptyBlock()
    else:
        try:
            return Block(json_result['id'], type, json_result['has_children'], json_result[type]['text'][0]['text']['content'], current_topic, json_result[type]['text'][0]['annotations']['bold'])
        except:
            return emptyBlock()

#(self, topic, sub_topic, question, answer_type, answer):
def defineQuestion(block, questions, current_topic):
    #initial variables to add to answer
    answer_type = ""
    answer = ""

    #gets the block children using the block children function, add adds a block at the end to allow the last block to be added as a question.
    block_children = getBlockChildren(block, current_topic)
    block_children.append(emptyBlock()) #a placeholder to stop an index error occurring
    answer = []

    for child in block_children:
        if child.is_answer:
            answer_type = child.block_type
            answer.append(child.content)
            try:
                if block_children[block_children.index(child) + 1].is_answer != True: #if the next block is not part of the current answer the question has finished
                    question = Question(block.topic, block.content, answer_type, ' '.join(answer))
                    question.SetAnswerType(answer_type) #changes the "paragraph" to "text"
                    questions.append(question)
            except:
                continue
        if child.has_children:
            #nested children haven't been iterated.
            defineQuestion(child, questions, current_topic)
    return questions

#copy of computer science
#https://www.notion.so/seanbendall/Copy-of-Computer-Science-fd532bfc5799420b84ac6285a0e419cd

#main function
def main():
    #getting all the pages from the main screen
    page_ids, topics = getPageIDs('fd532bfc5799420b84ac6285a0e419cd','all_pages')

    #gets the blocks from each page - only the first level blocks though.
    for id in page_ids:
        blocks = getBlocks(id, topics[page_ids.index(id)])
        print("\n\nQUESTIONS FOR " + topics[page_ids.index(id)] + "ARE \n\n")
        for block in blocks:
            questions_for_topic = defineQuestion(block, [], topics[page_ids.index(id)])
            for question in questions_for_topic:
                print(question)


#block ID for checksum block is https://www.notion.so/seanbendall/3-Data-Representation-f4e3f8367b01478b8fb6cef109ae9f86#31e170ba428441ad9b7720bee8b00d01


"""
test_block = Block("31e170ba-4284-41ad-9b77-20bee8b00d01", 'toggle', True, "What are the four techniques that can be used to check for errors in transmission?", "3 Data Representation", "#2 Bytes, Bits and Binary", False)
blocks = []
questions = defineQuestion(test_block, [])
for question in questions:
    print(question)
"""
main()
