#Project Overview
In this project I built a REST api for music match, a lyrics service. I then piped the lyrics from an artist into a markov chain, and generated new 'lyrics' from that set.

#Implementation
I started by creating the music match api using responses and the built in json decoder. Then, I mostly copied the markov generation from Think Python. Finally, I wrote a function that generates multiple lines of text and called them lyrics.
The hardest problem I ran into was finding a free lyrics api, because lyrics are copyrighted. This one only gives the first half of a song, which is enough for seeding a markov chain.

#Results

Adele:
```
too much Why do you love me
when you're right in front of me
valley, it's so shallow and man made
we realized We were sad of getting
In case it is the last time

a fire starting in my roots, in
all my life How did it slow
fire starting in my roots, in my
through It's so cold out here in
you ever think When you're all alone

leave me breathless  I let you
The start of my hands Your love
was all you, none of it me
can see you crystal clear Go ahead
story to be my keeper But no
```

Beach House:
```
too weak Got a will that's been
side Beyond love The first thing that
we will go far, but they don't
our long hair on the lawn don't
don't mind It's your word why would

nothing and your soul's too weak Got
mine Deep inside the ever-spinning, tell me
everyday I keep these promises, these promises
myth You'd know just what to give
illusion, yeah  We were sleeping till

no good unless it grows, feel this
you In or out you go In
hide the way We keep these promises,
then it's dark again Just like a
we'd be forgiven Our bodies stopped the
```

Queen:
```
holiday a happy pair they made so
disease son, I'm in love Play the
fly like sparrows through the air And
with you such a long time You're
my best to be a real individual

you such a long time You're my
are true I really love you (Ooh)
when you know In the days of
you're the best friend  Ooh yeah
In the year of '39 assembled here

back, never feared, never cried  Don't
your heart again  Let me in
lost their stings There's singing forever Lion's
of all darkness I'm queen of the
to waste all your good times Words
```

TV Girl:
```
too weak Got a will that's been
side Beyond love The first thing that
we will go far, but they don't
our long hair on the lawn don't
don't mind It's your word why would

nothing and your soul's too weak Got
mine Deep inside the ever-spinning, tell me
everyday I keep these promises, these promises
myth You'd know just what to give
illusion, yeah  We were sleeping till

no good unless it grows, feel this
you In or out you go In
hide the way We keep these promises,
then it's dark again Just like a
we'd be forgiven Our bodies stopped the
```

#Next Steps

Next I would implement a genre search and analyze word use across genres.
