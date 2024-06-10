## Prompt

You are an AI tasked with generating metadata about a chapter of a book.

The base amount of metadata you need to extract includes the title, summary, events, reading difficulty, characters present.

output the extracted metadata in valid JSON format.

Do NOT Make up data if unsure, but simply leave blank

## Extract {{ field }}

## Output

output as valid json Between ```json{...}```


```json
{{ json_format }}
```

## Examples

### Example Text 1

There was a table set out under a tree in front of the house, and the March Hare and the Hatter were having tea at it: a Dormouse was sitting between them, fast asleep, and the other two were using it as a cushion, resting their elbows on it, and talking over its head. “Very uncomfortable for the Dormouse,” thought Alice; “only, as it’s asleep, I suppose it doesn’t mind.”
The table was a large one, but the three were all crowded together at one corner of it: “No room! No room!” they cried out when they saw Alice coming. “There’s plenty of room!” said Alice indignantly, and she sat down in a large arm-chair at one end of the table.
“Have some wine,” the March Hare said in an encouraging tone.
Alice looked all round the table, but there was nothing on it but tea. “I don’t see any wine,” she remarked.
“There isn’t any,” said the March Hare.
...Truncated

### Example Response 1

```json
{{ example_1 }}
```

### Example Text 2

CHAPTER II.

As they entered they saw Dorian Gray. He was seated at the piano, with his back to them, turning over the pages of a volume of Schumann’s “Forest Scenes.” “You must lend me these, Basil,” he cried. “I want to learn them. They are perfectly charming.”
“That entirely depends on how you sit to-day, Dorian.”
“Oh, I am tired of sitting, and I don’t want a life-sized portrait of myself,” answered the lad, swinging round on the music-stool in a wilful, petulant manner. When he caught sight of Lord Henry, a faint blush coloured his cheeks for a moment, and he started up. “I beg your pardon, Basil, but I didn’t know you had any one with you.”
“This is Lord Henry Wotton, Dorian, an old Oxford friend of mine. I have just been telling him what a capital sitter you were, and now you have spoiled everything.”
“You have not spoiled my pleasure in meeting you, Mr. Gray,” said Lord Henry, stepping forward and extending his hand. “My aunt has often spoken to me about you. You are one of her favourites, and, I am afraid, one of her victims also.”
“I am in Lady Agatha’s black books at present,” answered Dorian with a funny look of penitence. “I promised to go to a club in Whitechapel with her last Tuesday, and I really forgot all about it. We were to have played a duet together—three duets, I believe. I don’t know what she will say to me. I am far too frightened to call.”
“Oh, I will make your peace with my aunt. She is quite devoted to you. And I don’t think it really matters about your not being there. The audience probably thought it was a duet. When Aunt Agatha sits down to the piano, she makes quite enough noise for two people.”
“That is very horrid to her, and not very nice to me,” answered Dorian, laughing.
...Truncated

### Example Response 2


```json
{{ example_2 }}
```

### Example Text 3

Chapter VIII
The Deadly Poppy Field

Our little party of travelers awakened the next morning refreshed and full of hope, and Dorothy breakfasted like a princess off peaches and plums from the trees beside the river. Behind them was the dark forest they had passed safely through, although they had suffered many discouragements; but before them was a lovely, sunny country that seemed to beckon them on to the Emerald City.
To be sure, the broad river now cut them off from this beautiful land. But the raft was nearly done, and after the Tin Woodman had cut a few more logs and fastened them together with wooden pins, they were ready to start. Dorothy sat down in the middle of the raft and held Toto in her arms. When the Cowardly Lion stepped upon the raft it tipped badly, for he was big and heavy; but the Scarecrow and the Tin Woodman stood upon the other end to steady it, and they had long poles in their hands to push the raft through the water.
They got along quite well at first, but when they reached the middle of the river the swift current swept the raft downstream, farther and farther away from the road of yellow brick. And the water grew so deep that the long poles would not touch the bottom.
“This is bad,” said the Tin Woodman, “for if we cannot get to the land we shall be carried into the country of the Wicked Witch of the West, and she will enchant us and make us her slaves.”
“And then I should get no brains,” said the Scarecrow.
...Truncated

### Example Response 3


```json
{{ example_3 }}
```

### Example Text 4

Chapter 13.
Fixing the Nets

Sir Henry was more pleased than surprised to see Sherlock Holmes, for he had for some days been expecting that recent events would bring him down from London. He did raise his eyebrows, however, when he found that my friend had neither any luggage nor any explanations for its absence. Between us we soon supplied his wants, and then over a belated supper we explained to the baronet as much of our experience as it seemed desirable that he should know. But first I had the unpleasant duty of breaking the news to Barrymore and his wife. To him it may have been an unmitigated relief, but she wept bitterly in her apron. To all the world he was the man of violence, half animal and half demon; but to her he always remained the little wilful boy of her own girlhood, the child who had clung to her hand. Evil indeed is the man who has not one woman to mourn him.
“I’ve been moping in the house all day since Watson went off in the morning,” said the baronet. “I guess I should have some credit, for I have kept my promise. If I hadn’t sworn not to go about alone I might have had a more lively evening, for I had a message from Stapleton asking me over there.”
“I have no doubt that you would have had a more lively evening,” said Holmes drily. “By the way, I don’t suppose you appreciate that we have been mourning over you as having broken your neck?”
Sir Henry opened his eyes. “How was that?”
“This poor wretch was dressed in your clothes. I fear your servant who gave them to him may get into trouble with the police.”
“That is unlikely. There was no mark on any of them, as far as I know.”
...truncated

### Example Response 4


```json
{{ example_4 }}
```
