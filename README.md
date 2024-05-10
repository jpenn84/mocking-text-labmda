# Mocking Text Project - Lambda

The Mocking Text Project is a simple serverless example project that uses serverless architecture and a web frontend for easily turning normal text into mmocking text.

The Mocking Text Project is a web application which makes REST requests to change text, allowing a user to convert their text from any device with a web browser.

## Explanation of Mocking Text

Mocking text comes from a meme of SpongeBob SquarePants scene, acting like a chicken due to hypnosis, where the still frame looks like SpongeBob is mocking someone.

**Example**

Input: ` Money can't buy happiness.`

Output: `MoNeY cAn'T bUy HaPpInEsS.`

## Limitations

The current limitations on what characters' case can be changed is limited by the Unicode Standard, as described in section 3.13 "Default Case Folding." (https://www.unicode.org/versions/Unicode15.0.0/ch03.pdf#page=86)

## API vs Client-Side function

While the same expected results can be made as a JS function and be made fully client-side, the use of an API allows for future expansion, such as training AI models or data collection.
## Authors

- [@jpenn84](https://www.github.com/jpenn84)


## Badges

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-limegreen.svg)](https://opensource.org/licenses/)
