Game id, for each game
Version, for each game
Info fields, up to 30, all start with info
Start fields, 18 or 20, lists players
  Player Attributes (5)
    1. Unique 8 digit code
    2. Player Name
    3. Home field indicator: 0 for visitors, 1 for home
    4. Batting order
    5. Field position, google it, (10 for DHs)
Play Records
  Play Attributes (7)
    1. Inning Number
    2. Home field indicator: 0 for visitors, 1 for home
    3. Player Attributes Unique 8 digit code
    4. Count when event occurred, "??" when not available
    5. All pitches, blank if unavailable
      1. B  ball
      2. C  called strike
      3. F  foul
      4. H  hit batter
      5. I  intentional ball
      6. K  strike (unknown type)
      7. L  foul bunt
      8. M  missed bunt attempt
      9. N  no pitch (on balks and interference calls)
      10. O  foul tip on bunt
      11. P  pitchout
      12. Q  swinging on pitchout
      13. R  foul ball on pitchout
      14. S  swinging strike
      15. T  foul tip
      16. U  unknown or missed pitch
      17. V  called ball because pitcher went to his mouth
      18. X  ball put into play by batter
      19. Y  ball put into play on pitchout
      20. Other
        +  following pickoff throw by the catcher
        *  indicates the following pitch was blocked by the catcher
        .  marker for play not involving the batter
        1  pickoff throw to first
        2  pickoff throw to second
        3  pickoff throw to third
        `>  Indicates a runner going on the pitch`
    6. Play events
      Listed as NP when signaling a sub incoming
Com, plays requiring special comment
Sub, substitution event
  Sub Attributes
    1. Player Attributes Unique 8 digit code
    2. Player name
    3. Home field indicator: 0 for visitors, 1 for home
    4. Batting order positon of sub
    5. Field position, 11 for pinch hitter, 12 for pinch runner
Data Fields
  Could be used to calculate total runs by each team when
  Fails in some cases: ANA201805180
  Could be used to help validate other guesses
