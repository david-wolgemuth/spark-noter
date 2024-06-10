#! /usr/bin/env python3

from openai import OpenAI
import bs4
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json


templates = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['md'])
)


def chat_completion(
    system_prompt: str,
    user_prompt: str,
) -> str:
    """
    https://platform.openai.com/docs/api-reference/chat/create

    system_prompt: The system instruction to the Chat Completion API.
    user_prompt: The "user" context, i.e. the book content.
    """
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        # model="gpt-4o-2024-05-13",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return completion.choices[0].message.content


# def chat_completion(
#     system_prompt: str,
#     user_prompt: str,
# ) -> str:
#     """
#     """

EXAMPLES = [
 {
  "title": "A Mad Tea-Party",
  "summary": "In 'A Mad Tea-Party,' Alice encounters the March Hare, the Hatter, and the Dormouse having tea under a tree. The Dormouse is asleep and used as a cushion by the other two. Alice joins the tea party despite being told there's no room. They offer her non-existent wine, leading to a series of nonsensical conversations. The Hatter asks Alice a riddle about a raven and a writing-desk, which he doesn't know the answer to. They discuss the concept of Time and its peculiarities. The Hatter and the March Hare explain that it's always tea-time for them due to a quarrel with Time. The Dormouse tells a disjointed story about three sisters living in a treacle-well, drawing treacle and other things that begin with the letter 'M'. The chaotic and confusing tea party ends with Alice leaving in frustration and finding herself back in the long hall, ready to explore the beautiful garden.",
  "events": [
    "Alice joins the tea party",
    "Conversation about non-existent wine",
    "Riddle about a raven and a writing-desk",
    "Discussion on Time",
    "Story about three sisters in a treacle-well",
    "Alice leaves the tea party"
  ],
  "reading_difficulty": "Grade 6",
  "characters": [
    "Alice",
    "March Hare",
    "Hatter",
    "Dormouse"
  ]
},
{
  "title": "Chapter II",
  "summary": "In Chapter II, Dorian Gray is introduced while seated at a piano, expressing his desire to learn Schumann’s 'Forest Scenes.' He interacts with Basil Hallward, the artist painting his portrait, and meets Lord Henry Wotton, Basil's friend. Lord Henry quickly captivates Dorian with his provocative views on life and beauty. He argues that all influence is immoral and extols the virtues of self-development and indulgence in sensory pleasures. Dorian is deeply affected by Lord Henry’s philosophy, realizing for the first time the transient nature of his youth and beauty. This leads to a moment of existential reflection and a desire to retain his youthful appearance forever, even at the cost of his soul. The chapter concludes with Dorian insisting that Lord Henry stays during the painting session, further cementing the influence Henry has over him.",
  "events": [
    "Dorian Gray is introduced at the piano",
    "Dorian expresses desire to learn Schumann's 'Forest Scenes'",
    "Introduction of Lord Henry Wotton",
    "Lord Henry captivates Dorian with his philosophy",
    "Dorian reflects on the transient nature of youth and beauty",
    "Dorian wishes to retain his youthful appearance forever",
    "Dorian insists Lord Henry stays during the painting session"
  ],
  "reading_difficulty": "Grade 10",
  "characters": [
    "Dorian Gray",
    "Basil Hallward",
    "Lord Henry Wotton"
  ]
},
{
  "title": "Chapter VIII: The Deadly Poppy Field",
  "summary": "In this chapter, Dorothy and her companions wake up refreshed and continue their journey to the Emerald City. They construct a raft to cross a broad river, but the strong current sweeps them downstream, separating them from the Scarecrow. The Cowardly Lion swims to shore, pulling the raft and saving the others. A Stork rescues the Scarecrow, and they continue their journey. They encounter a field of deadly poppies whose scent puts Dorothy, Toto, and the Lion to sleep. The Tin Woodman and Scarecrow carry Dorothy and Toto out of the poppy field, while the Lion remains asleep, unable to be moved due to his size.",
  "events": [
    "Travelers wake up refreshed",
    "Construct and board a raft",
    "Swept downstream by the river",
    "Scarecrow left clinging to a pole",
    "Cowardly Lion swims to shore",
    "Stork rescues the Scarecrow",
    "Encounter a field of deadly poppies",
    "Dorothy, Toto, and Lion fall asleep",
    "Tin Woodman and Scarecrow carry Dorothy and Toto to safety"
  ],
  "reading_difficulty": "Grade 4",
  "characters": [
    "Dorothy",
    "Tin Woodman",
    "Scarecrow",
    "Cowardly Lion",
    "Toto",
    "Stork"
  ]
},
{
  "title": "Chapter 13: Fixing the Nets",
  "summary": "In this chapter, Sherlock Holmes arrives unexpectedly at Baskerville Hall and joins Sir Henry and Dr. Watson. Holmes and Watson recount their recent experiences to Sir Henry and break the news of Selden’s death to Barrymore and his wife. Holmes is intrigued by the family portraits, especially one of Hugo Baskerville, which resembles Stapleton. Holmes devises a plan to trap Stapleton by pretending to leave for London while secretly returning to capture him. He convinces Sir Henry to attend a dinner at Stapleton's house alone. Holmes and Watson visit Mrs. Laura Lyons, who reveals Stapleton’s deceit and her unwitting involvement in his schemes. Holmes and Watson prepare for their final move against Stapleton with the assistance of Inspector Lestrade.",
  "events": [
    "Sherlock Holmes arrives at Baskerville Hall",
    "Holmes and Watson recount their experiences to Sir Henry",
    "News of Selden’s death is broken to Barrymore and his wife",
    "Holmes examines family portraits, noting Hugo Baskerville’s resemblance to Stapleton",
    "Holmes devises a plan to trap Stapleton",
    "Sir Henry is convinced to attend a dinner at Stapleton's house",
    "Holmes and Watson visit Mrs. Laura Lyons",
    "Mrs. Lyons reveals Stapleton’s deceit",
    "Inspector Lestrade arrives to assist in the investigation"
  ],
  "reading_difficulty": "Grade 10",
  "characters": [
    "Sherlock Holmes",
    "Dr. Watson",
    "Sir Henry Baskerville",
    "Barrymore",
    "Mrs. Barrymore",
    "Stapleton",
    "Mrs. Laura Lyons",
    "Inspector Lestrade"
  ]
}
]

def generate_chapter_summary(
    book_metadata: dict,
    chapter_body: str,
):
    """
    generate summary for a chapter
    """
    chapter_metadata = {
    }

    for field, json_format, examples in [
        [
            "title",
            '{"title": String}',
            [{"title": e["title"]} for e in EXAMPLES]
        ],
        [
            "summary",
            '{"summary": String}',
            [{"summary": e["summary"]} for e in EXAMPLES]
        ],
        [
            "events",
            '{"events": Array<String>}',
            [{"events": e["events"]} for e in EXAMPLES]
        ],
        [
            "reading_difficulty",
            '{"reading_difficulty": String}',
            [{"reading_difficulty": e["reading_difficulty"]} for e in EXAMPLES]
        ],
        [
            "characters",
            '{"characters": Array<String>}',
            [{"characters": e["characters"]} for e in EXAMPLES]
        ],
    ]:
        retries = 3
        for i in range(retries):
            try:
                chat_completion_response = chat_completion(
                    system_prompt=templates.get_template("chapter_summary_system.md").render({
                        "field": field,
                        "json_format": json_format,
                        "example_1": json.dumps(examples[0]),
                        "example_2": json.dumps(examples[1]),
                        "example_3": json.dumps(examples[2]),
                        "example_4": json.dumps(examples[3]),
                    }),
                    user_prompt=templates.get_template("chapter_summary_user.md").render({
                        "chapter_body": chapter_body,
                    }),
                )
                json_str = chat_completion_response.split("```json")[1].split("```")[0]
                data = json.loads(json_str)
                chapter_metadata.update(data)
                break
            except Exception as e:
                print(e)
                print("retrying...")

    return chapter_metadata


def generate_book_metadata(book_html: str) -> dict:
    """
    """

    FIRST_PAGE = 4000  # roughly the size of a page ???
    first_page = book_html[:FIRST_PAGE]

    chat_completion_response = chat_completion(
        system_prompt=templates.get_template("book_metadata_system.md").render(),
        user_prompt=templates.get_template("book_metadata_user.md").render({
            "first_page": first_page,
        }),
    )

    # print(chat_completion_response)

    json_str = chat_completion_response.split("```json")[1].split("```")[0]
    return json.loads(json_str)


def generate_book_summaries(file):
    """
    split book into chapters (<div class="chapter">(...)</div>)
    and generate summary for each chapter
    """
    book_html = file.read()

    book_metadata = generate_book_metadata(book_html)
    print("generated book metadata", book_metadata)

    soup = bs4.BeautifulSoup(book_html, "html.parser")

    chapters_html = soup.find_all("div", class_="chapter")
    if not chapters_html:
        raise Exception("No chapters found")

    chapters_summary = []
    retries = 3
    for chapter in chapters_html:
        chapters_summary.append(
            generate_chapter_summary(
                book_metadata=book_metadata,
                chapter_body=str(chapter),
            )
        )
        print("generated chapter summary", chapters_summary[-1])

    return {
        **book_metadata,
        "chapters": chapters_summary,
    }


def write_to_file(file, book_metadata: dict):
    """
    write book metadata and summaries to file
    """
    file.write(templates.get_template("book_summary.html").render(book_metadata))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input",
        type=argparse.FileType("r"),
        help="path to the book",
    )

    parser.add_argument(
        "output",
        type=argparse.FileType("w"),
        help="path to the book",
    )

    args = parser.parse_args()

    book_metadata = generate_book_summaries(args.input)

    print(book_metadata)

    write_to_file(args.output, book_metadata)
