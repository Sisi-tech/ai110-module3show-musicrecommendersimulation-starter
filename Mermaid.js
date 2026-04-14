```mermaid
graph TD
    A[Input: User Preferences] --> B[Load Songs from CSV]
    B --> C[Process: Loop through each song]
    C --> D[Score individual song using scoring logic]
    D --> E[Collect score and reasons for each song]
    E --> F[Rank all songs by score descending]
    F --> G[Select top K recommendations]
    G --> H[Output: Ranked list of top K songs with scores and explanations]
```
