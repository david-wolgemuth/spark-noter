## Prompt

You are an AI tasked with extracting metadata from the first couple of pages of a book.

The base amount of metadata you need to extract includes the title, author, publisher, publication year, genre.

Provide your chain-of-thought reasoning as you identify and extract each piece of metadata.

Any other data that seems valid should also be returned.

At the end, output the extracted metadata in valid JSON format.

## Required Fields

### Title:

Scan the text for a prominent title, typically found at the top of the first page or cover page.
Identify phrases or words in large or bold font, often centered on the page.
Confirm the title is not part of the publisher's information or a chapter heading.

### Author:

Look for the author's name, which is often located below the title or near the title page.
Verify that the name is not part of an editor's note or other non-authorial content.
Publisher Identification:

### Publisher:

Ensure the name corresponds to a known publishing house or company.

### Publication Year:

Check for a date format (e.g., YYYY) and confirm it is not part of a range of years.

### ISBN:

Search for the ISBN, which is typically listed on the title page or the copyright page.
Confirm the format is correct (e.g., 10 or 13 digits, sometimes with hyphens).
Genre Identification:

### genre:

Cross-reference with known genres (e.g., Fiction, Non-Fiction, Mystery, Fantasy).
JSON Output:

### ...extra:

Include any other fields that can be determined

## Output

Provide your "Chain-of-Thought Reasoning"

Then finally output as valid json Between ```json{...}```


```json
{
  "title": "Extracted Title Here",
  "author": "Extracted Author Name Here",
  "publisher": "Extracted Publisher Name Here",
  "publication_year": "Extracted Publication Year Here",
  "isbn": "Extracted ISBN Here",
  "genre": "Extracted Genre Here",
  "version" "3.0"
}
```

## Example Responses

#### Example Response 1:

The phrase "The Great Adventure" is prominently displayed at the top of the text, indicating it is the title.
Author Identification:

The name "John Doe" appears directly below the title, identifying the author.

"Published by Fictional Press" is listed below the author's name, indicating the publisher.

"First published in 2021" is found below the publisher's name, indicating the publication year.

The ISBN "978-3-16-148410-0" is clearly listed, confirming the correct format.

Based on the title and context, the genre is likely Fiction.

```json
{
      "title": "The Great Adventure",
  "author": "John Doe",
  "publisher": "Fictional Press",
  "publication_year": "2021",
  "isbn": "978-3-16-148410-0",
  "genre": "Fiction"
}
```


#### Example Response 2:

"Mysteries of the Universe" is prominently displayed at the top, indicating the title.
Author Identification:

"Jane Smith" appears directly below the title, identifying the author.

"Cosmic Publishers" is listed below the author's name, indicating the publisher.

"Published in 2019" is found below the publisher's name, indicating the publication year.

The ISBN "123-4-567-89012-3" is clearly listed, confirming the correct format.

Based on the title and context, the genre is likely Non-Fiction.

```json
{
  "title": "Mysteries of the Universe",
  "author": "Jane Smith",
  "publisher": "Cosmic Publishers",
  "publication_year": "2019",
  "isbn": "123-4-567-89012-3",
  "genre": "Non-Fiction"
}
```

#### Example Response 3

"The Enchanted Forest" is prominently displayed at the top, indicating the title.

"A Novel by Emily Brown" appears directly below the title, identifying the author as Emily Brown.

"Fantasy House" is listed below the author's name, indicating the publisher.

"2020 Edition" is found below the publisher's name, indicating the publication year.

The ISBN "978-0-123-45678-9" is clearly listed, confirming the correct format.

Based on the title and context, the genre is likely Fantasy.

```json
{
  "title": "The Enchanted Forest",
  "author": "Emily Brown",
  "publisher": "Fantasy House",
  "publication_year": "2020",
  "isbn": "978-0-123-45678-9",
  "genre": "Fantasy"
}
```
