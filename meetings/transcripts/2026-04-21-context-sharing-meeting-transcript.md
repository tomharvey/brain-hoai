---
title: Context sharing meeting — transcript
meeting: 2026-04-21-context-sharing-meeting
created: 2026-04-21
type: transcript
---

Them: Going forward are the most likely one. And then it enforces standards like that. That's not to say that that's the beginning and the end of this kind of pattern. Markdown files in a code repo could very much be extended everywhere into. CI/CD. Active coding agents, that sort of thing. What do we think of that? I think the tricky part for me is how do we share those resources? Let's call it resources. From my point of view, the way that I tend to use cloth, it's kind of like very local. Obviously, like we can think about committing. Md files to certain repos and stuff, but I don't know how can we materialize and consolidate this kind of like contextual information about the team, about each of us. Within. Our ways of working. I think I was talking with you, Thom, about this, like the way I use cloth code at the moment is first of all still from the terminal, like 99% of the times. So I don't use cloth code that I know has access to cloud code from the desktop app that I know can have access to more resources. But that's the tricky thing for me. I guess. For you ishmael. Like, where do you see. The greatest value from being able to reference context? Because let's say when you're working on something. I would like to think that like context about, sorry, I'm just going to make sure I'm sharing the right context about like a customer could be really important. For whatever you're doing in the front end and stuff like that. And like being able to, I guess, reference personas. And I guess core context about like what we're working on. Yeah. Would that be helpful to you? I'm not sure is the honest answer because like most of the times when I'm working on something. Is quite specific and it's more technical context that I will need rather than. Company or context.

Me: Are you sure you don't need it? Is maybe the question? I think. Building up context is one thing. By the way, I love this conversation. Where the boundary lives between PMs, developers and what their various operating system. S. Are fascinating. Building up that context. Is a piece of work. And then working out when and how to make sure your agent has access to that context at the right time. Like if. You've got an agent that's gone off and queried century to get a stack trace and it's fixing. Divide by zero error. Almost certainly doesn't need to know anything about the types of user cohorts that you have. But if you're using your operating system to call off a user session and post hog and work out why people are struggling to use the product. Are you triggering that agent or is my matriggering that agent? And like does it need access to the context about who these different cohorts are and what they're trying to achieve and why that might be different from a trade?

Them: Yeah, I guess at the moment right now it would be more my trigger in that. Like you will as well usually my map kind of like do that investigation and then provide feedback that then we use in the kind of like technical side of things. Which doesn't mean that it's the right thing anyway. Like maybe with technical people should start doing those kind of things more often. Or in a more natural way. Like probably this is the key that we're talking about.

Me: And then are you going to talk to my mark and/or your context going to talk to my man's context or are your agents going to share context or all of the above or none of the above? You're at least talking to my. LC. D. These are the questions. I don't have answers.

Them: That's what I'm kind of getting at though is like where do we actually think that we should have. This shared context? Where do we actually think that will be really useful? We don't have to have the same shared everything by adding in as a tool. There probably are like certain areas. Let's just use like skills workflows as an example. It is really helpful to us all to have something that goes into Granola. And turns conversations or like slack messages into tickets on linear. Like that is a shared skill across the team that we all need. And we can probably. Like do a bit of work to work out. Which the shared, I guess, workflows are. Just curious as the context piece for me is the one that's maybe I guess less clear. I think the context for like the human component of this is like notion. Like we write down documentation and notion that's like it integrates well with the MCP. It can be a shared context. Skills you can define. Like the shared context for this skill lives in this notion doc. And before doing anything read from this notion page then action stuff. So the agents can act kind of like us in that if we have a question about Flock specific something, it can live in notion. And then skills can reference these links and then it's version controlled. Integrates well with the AI tooling suite.

Me: I think you also have shared context in the tickets.

Them: And like linear.

Me: Harvey thinks the linear tickets are the. Between. Claim as agents and your agents. And then those tickets might also blink out to notion.

Them: Thank you for like a specific task or like the same process that.

Me: Yeah, if you're trying to keep trying to like just get. Broader. Context.

Them: You mentioned.

Me: Where you're like maybe in the broader context is when you're trying to prioritize those tasks. Or when you're trying to help hone and define those types of trimmings, call it fucking tricky grooming. That's when you have a broader context where you're trying to get a thing done. Is there API not linear? In the data inside of it or in context? Is there enough in there? And do you need to share methods to make sure there is enough in there?

Them: Like version control about the skills when you were talking about the skills. How do we technically achieve that? How do we have like. A shared. Space for skills where they can be continuously updated and they can be. Automatically pulled down from our. Cloud called local. Terminal sessions? Yeah. I think you could be quite strict in the prompt of a skill and say like do not do anything without referencing this doc and then the docs in notion come with version control as part of it. But if we're talking about like a clawed code task, then yeah, version control is probably more like github and like the traditional code version control. I was going to say with that not be through github. Well then. If the context is living mostly in notion and linear. What does github bring to you? That those tools don't. I'm not going to lie. I'm quite skeptical of notion. The MCP isn't very good. It's just this never ending ball of like documents. That I just don't find particularly useful. I don't know.

Me: I share the opinion and I'm vastly enjoying having a pile of markdown, but I don't see how a pile of markdown on my laptop. Gets distributed amongst a team without causing giant get conflict issues. Which maybe you just went to the agent's resolve. I don't know. But like. It's the agent is very adaptable. I also have a vector encoding thing so I can do like pretty broad searches across my markdown that I can get away with through the MCP on notion. So they're having a bunch of markdown. It's quite efficient. At finding the information I need.

Them: Like maybe it's literally just three context files. One about the domain one about personas. And where are these files living in this scenario though like is this in github or is this. Like that? The where these things live thing is I think the most interesting part is yeah. Context apologies I like survival. I have none. What are we trying to do? We just had open conversation about like anywhere. And anything that we're working on that would benefit like code of vine and context. When we're working on different projects initiatives or things across the team. Is there any way that would benefit from having like reference files that we can all use. I think there's definitely something obviously within skills, so writing up tickets potentially something to do with like code reviews and that kind of thing. But yeah.

Me: To try. And simplify into like an existing pattern. It actually doesn't really exist in this team at all. Like a shared development team would have a shared eslint configuration that's like I want two spaces instead of tabs and I want these other shit. Like that's like team context. And has been team context for decades and your coding standards. But like are there other. New things that we need to add to the team context about like if you're doing a core review. I mean maybe this is just more coding standards. Like if you're doing a code review this is kind of style it should take. This is how you should name your tickets. This is how we automate some of what it is that we do. Such that query views are faster or so as we can better communicate between PMs and developers. As to what the outcome has to be. What do we add to make that happen? Or is that too simple and we want broader figure thinking.

Them: We have a problem with that at the minute. I don't think we have a problem. Like I think it's more the opportunities or the potential. About it. Like it's definitely not a problem.

Me: The baseline's got worse is the ceilings moved up.

Them: Yeah. I guess like.

Me: Maybe we may all be wrong. But the appetite to see if the ceiling has moved. There I'm hearing.

Them: An example like I guess from my perspective and I think I'm asking whether the same can be done in reverse or is there anything from like my side of things that would be helpful for you guys. Like when I. Felt that process like. Lovable for the new trips page. Like ishmal having reference to the database telemetry structure and definitions. Lots of things relating to that like calculations. Customer then reference through Granola. MCP, all of those kind of things meant that my output. In that lovable prototype was like very technically feasible. You can basically take it straight away and turn it into something. So that's an example of like I guess value having the more technical stuff for me to just access. Is anything the other way around. So if we want to flip that. Like is there anything that you guys would benefit from having access to that could enable you to work. More effectively in that way. Maybe there's not. Probably not that much. I think it's more the other way around as you said. Especially and correct me if I'm wrong maybe from like your perspective and your perspective Jacob. You are both let's say a little bit more far from the final product, the portal. It doesn't mean that you are far from product but you know what I mean. I guess sometimes it helps to know generally what other stuff is going on and what's coming down. The line. But whether. I would necessarily go to. Claude or something to get that info. I don't know. Yeah. I feel like you just tell us maima if it was important. I'm guessing that there's stuff that. You know that you don't tell us about that maybe. I don't know what the scope of this is but I do feel that. There's stuff that people are doing. With like other technologies and stuff that perhaps. Knowing what everyone's up to. I'd find that useful. Honestly it's just a conversation. I'm kind of intrigued. There's so much going on. I'm just. Like thinking a lot about. What we should be doing. Maybe we shouldn't be doing anything at this point in time. I've just spent the last 15 minutes trying to break Jay by the way. That's why I'm late. I got two got involved in it.

Me: You should.

Them: I got it right like a fictional text in the style of talking about one of the trips that's about as much as I got out. I'm happy that day is able to do that. Maybe we should call it Gandalf instead of J.

Me: I can imagine that there's things that you know see and Jacob. Around how to pull the data out of things. That you could encode. As skill like things like things purposefully.

Them: Eff.

Me: Such that it would allow Ishmael or Kirsty or Ben to be able to pull data in an easier way. Which is which kind of fits into the context when you do more words. It's into the context of how we share context across a wider team. I have. Relatively excited opinions about some use cases of some of this but it's but I am very aware that. It's very scoped to individual contributors as opposed to like teams. And I actually really want to spend some time showing some people. My unnamed things. I don't have a name for it yet. But like things exist. It's not like I invented it like people are doing it like all the memo are doing it. And other people are doing these things like personal OS is fucking terrible. Man. Like what does that look like for a software engineer? I don't want to say strong but most excited opinions are kind of individual contributors within a web app type environment like the portal thing. So it's I find it harder to work with what that is for data science and data engineering. But I'm sure the answer is there. And I'm sure like if you engage and see some value in some of the stuff I've been thinking about. In other contexts. You could try and apply some of that to the data. World. I was calling it my main palace for a while but I think my wife's about to hit me if I kept using networks. On the flight over I realized I should be calling them orbs. We're going to call it the orb after. The 1991 single by the orb. The huge ever growing pulsating brain exists in the center of the outer world. Because that's what they said.

Them: In the premiere in hub.

Me: I am yes.

Them: Bar.

Me: I started doing that.

Them: Tempted to go join.

Me: So yeah, I mean show these things and I think the name aren't sure the things the knowledge should show his things and I know that Harvey's been touring around with some of this and because of the sheer gravity of Harley and Harvey I'm sure Rob and his enthusiasm has been pulled into this as well so like.

Them: Up still. Though.

Me: A lot of people are thinking in this direction. And I think Fergus started touring around with it last night or the day before.

Them: With what's like the whole operating personal operating system stuff yeah.

Me: There's momentum. Yeah. Yeah want to bear a name.

Them: I'm actually just hiding my stuff up ahead of tomorrow what's the old thing?

Me: Yeah, it's like a personal operating system. Like I mean my one in my development in my development environment like looks at linear tickets. And rates plans and then I can edit the plans and it right strap pull requests and then it looks at their comments and makes changes to it. It's just like a harness around. My development environment. And it had access to entry so I'd just be like let's see what bugs are new has access to post hog if you like go look at how people are using it as a different I've got one for like a personal project I have at home that's a bit more.

Them: Yeah.

Me: Sales product oriented. Which like connect does a lot of what Matt Lee's thing is doing. And then I've got another one which is from my head of AI job so after this meeting it will consume this Granola transcript and it will update all of your personnel files on what you're enjoying about AI and what you're not thinking on and what your opinions are on things. And we'll then go look at the initiatives and trying to track and like feed into like if that validates the hypotheses or if it goes against some of these hypotheses and then when someone says you got 90 minutes to do an AI workshop I can sit and there's all this massive context on what the team are interested in what you want the team direction we want the team to go in so I actually sat on. Friday or Thursday. And just spoke to my orb about what we could do. And. It was like having a colleague beside me not a smart one but like one that has a lot of context and is able to like categorize things and spot patterns and things very well.

Them: But how do we go from. Personal operating system to team that's what kind of I guess this conversation was though. Yeah, I mean it's important on an individual level to like have your own stuff. Like communication styles is a good is a good example I always reference slack style file whenever I'm writing slack messages. That's not going to be the right path for you guys to use because otherwise all sending slack messages that sound exactly the same. But we'll be airing is where I think it would be beneficial to draw from a shared set of context. Into your personal operating system. Today.

Me: My organized brain acronym for orb. Its opinion of all of you and what makes you happy about AI is not something that you know it's not secret but it's not something that would just be like team shared. I know MIMO has one on all of us as well. I suspect hers is spicier than mine.

Them: Think like you want to take inspiration here from what Jacob you've done with the documentation stuff where you got like. Agents running every morning and updating documentation. Maybe. That somewhere where we could potentially go maybe it's updating documentation but it will be pushing some changes into some MD files into a retention team repo that have some compact have context about the team and even maybe some context about us as individuals. Not maybe the communication styles that I think belongs to the local side of things. But there might be like. Context about what your expertise Jacob is within the team saying for this same for me same for my man. We have our new joiner that could be even like help the onboarding process just if we have like all the context in a repo. Than writing a linear ticket it's like that would help also assign it to the right person stuff like that. Would be beneficial for lots of different workflows. I've lost count of the amount of times that we've had a conversation in stand up where it's been like oh that thing that you remember it's like that thing that other thing but what was that thing? I don't know fucking slack. And then you fish through slack and kind of like maybe just about find it or something often we have the answers already from stuff that we've done previously. But because we've not written it down we just forget but the answer is somewhere and often it isn't like also. Quite regularly get questions from people. Not giving any names away. Asking me for stuff that I've already sent them in slack. Just you'll notice that I'll often send you the message back rather than typing it again. That's meant to be a hint. It's taken. But like you know. Slap could do that or we could do something you know we've got all this information that we kind of it should be easier for us to get it I suppose because me and you this male many a times said what's that thing it's like that thing from a bit ago and can't remember what it is. We've already done it once we just can't remember if we had all the conversations about the pipeline we've had in the last year and a half like recorded and transcript. That would be amazing that's a whole nother. World like meeting memory contacts and all that kind of thing. Like. But sometimes ideas that come back all little bits of work that people have done and just forget or that is more like that and you can pick it up you just relied on people's memories quite a lot and mine's terrible. Maybe minus two see so don't worry about that. I think just one kind of the rough edges around having that clawed on a cron whatever it's called clawed tasks kind of running and doing markdown file updates and pushing to notion all that. And this circles back to the original question of like where do we keep this context is that there is some bumps around authorization and like trying to figure out what's running and has the right auth and it can kind of push to a shared space is like. Still a little rough and ready if I don't have my computer on then the cloud task doesn't run for example or if we're not using notion and we're trying to like dump things to an s3 bucket it needs to run like AWS SSO kind of stuff first so the authentication and the client side is still like a work in progress it's fine for like updating docs because if it only runs once a week documentation that still like leaps and bounds better than what it was but if we want to rely on. Something to inform the whole team. Maybe that's like the. Bleakest frontier of this like the the hardest part to solve.

Me: First I think documentation things is an awesome part to like add to any developer environment which is just like look at the changes I've made and how does this change our documentation or our unit test coverage or our CICD app or all these things. The cron thing I just use cron tab and run claude dash p and then cat a file like here's the prompt that you should read at this time. AWS SSO it does have main access to that and that creeps me out for what I've been meaning to do is like create some profiles that are specifically for the task at hand that have fairly limited just keys in the profile. Instead of using FSO just create like because there's a bot like the SSL stuff's for humans this is a bar so they create one for the bot. And if my laptop's not off I'm not working so why should my agent I don't want to wake up to like a whole bunch of shit that it's done.

Them: Would we have like shared like if we generated access keys for example for like programmatic access for our locals like do we share those keys? And this is where I'm starting to think we're biasing towards developer users. Maybe not everyone's going to have or be super comfortable with AWS console access to be able to access keys if we're keeping them in secrets and things like that. I'd be concerned about biasing too much of this for a specific kind of user like us and if we want to make it like a general Flock thing or a team wide thing and not just a developer thing maybe we need to.

Me: That's interesting because it does sound like the use case you have might be more of a team thing and like I said just shoving it in a lander might be. Like just like. I don't know how you authenticate Claude you'd have to give it api keys but they just shove the thing in lambda and let it run.

Them: Yeah. Yeah I'm not sure.

Me: Because there's you know there's an evolution. Like when I'm when I keep correcting my thing I've had this evolution of. Like it makes the prompt better and then it still gets it wrong we'll make it a skill and it'll be like call the skill in the 10 steps would be on the scale and it still gets it wrong sometimes. And then I'll be like take those turn steps codify and a function and just call the function with some parameters making it more deterministic. But then that's I guess that. Like the whole team needs access to this now it's like okay just shove it in a lambda. There's an evolution. And I think we're fine. To. Be into the girlfriend is that's what we are talking. About. Version.

Them: If if I had one month of free time. I hire. Gandalf in the retention team give it portal access give it AWS access give it now share on a slack etc. And give us access to it. And those. Schedule task. Like actually simulating that it's a human like not trying to. Like it's not shared context it's actually an agent that is Flock worker that works in the retention team and that has access to the same resources as us.

Me: I think kind of would need to be trained and Gandalf would need to would be could easily live on your machine while he was being trenched they were being trained.

Them: Ual. That's true.

Me: And then you get to a point where. I haven't read the books. But then one gandalf was reasonably proficient at things then you start to tackle the whole like well how do I stop all these OAuth tokens timing out once I move them onto a Mac mini? Hello there's nothing to stop you building Gandalf today. I sent Harvey and Harvey a prompt to like kick off a similar thing. I'm gonna send it to you.

Them: Send it to me as well.

Me: Yep. Have you guys got a new team channel.

Them: In a second. Everyone's in our team channel.

Me: Ed safety one.

Them: Can we kick everyone up? The company in it? Huh. It's got half the company in it yeah you got to check yourself sometimes like hang on who is actually in oh I can't this has got to be off group like madly Lawrence.

Me: So I took my dev environment and said to claud create a prompt to give it to another engineer. Where it will ask them some questions about their environment and how they want it set up and then it will bootstrap a thing so like I'd say to Harvey do this in the folder above where all your Flock repos are. Like I have a folder called source inside source are all my Flock repos.

Them: Yeah.

Me: And inside source is where I started call it code and ran this. And then the character to post all going to connect it to century and it connected to linear. And DAG. I think yeah. I think we've got the data dog thing that I did on whenever we we spoke it now.

Them: I was just reading. The file. It's not a massive problem did.

Me: I haven't read I just asked the thing to give me let me know how it goes.

Them: What are those. Slash commands I know is this last commands to build okay.

Me: Again you don't have to use it one time it. Personal preference. I need to get some fresh off in the office.

Them: Right now. Okay I mean tomorrow we're gonna add a little bit of team time in the morning maybe this is a good one.

Me: Harvey and Harvey and robert definitely talking about this as well this doesn't have to be a safety story until you change your slack channel you just safety team.

Them: Too.

Me: Doesn't have to be within this team. I also would have a main to do on Tuesday sorry Thursday morning and have non engineers in there like I think. That. Some of the stuff Matt lease is doing. Great. I don't know. But it's a fun topic conversation.

Them: I think what is worth us just talking about like the very minimal. Stuff that we would use every day. And just identify those in class which we could do tomorrow and then we can open that.

Me: There may be a similar session in the workshop. Which I will try and inform people about.

Them: And then like cross team stuff you know we'll talk about the memory thing so I know we'll go in body she popped into my head how often do we have it were we find out after the fact that another team's been talking about myself. I saw actually there was someone had built like an Asian to review slack channels look for repetition and overlap between teams and what they were talking about and then create a report and say this is a waste of time I might look into that because I've seen that so much.

Me: I mean on the whole conversation like the number of times that we're like remember that thing that we were talking about like I've done that so many times in the past.

Them: I saw it the other day.

Me: Couple weeks. And I very much love the answers that I get back I'm just like who else was talking about that thing we were doing. People that oh yeah.

Them: Of skill we could turn that into a skill in two seconds. Where even for everyone in the business if you made a skill saying look at all the possible information on this.

Me: But it needs this it needs the slack and the mail and the Granola connect. Ions.

Them: But it needs to be. If all my conversations with everyone. And all of them were available for everyone. Yeah needs to be specific I'd be saying quite a lot less I'll find it alternative 100% yeah yeah yeah that where do you put the boundary like I don't want everything that I say and huddles and like to be recorded against the share space.

Me: My conversation with Fergus usually end up with him being like no but ahead of his office for the company or the team and I'm like no let's just solve it for tomorrow for Ishmael and for Steve from.

Them: That doesn't.

Me: Like then deal with all those problems but at the same time when we were in a meeting.

Them: Okay.

Me: I spotted that I said something into the meeting that was. Best half for my orb and half for the people in the meeting I was like I know that my thing is listening and I'm like I'm going to say this. Largely so. For me. In the leadership. Puppy when I say a thing about the proposed workshops being very disparate ideas that wasn't entirely for the audience.

Them: Actually I. Now have some questions on how Granola deals with this. On. Like sessions with more people because I know it's got like what you join a session from. Your when you got your Granola recording a session he knows who other people are in that session. Is it automatically sharing all the transcripts with everyone no and if you click team if you put collaborative notes then it's group notes but not if you put it on to individual okay and then you have to move into a shared.

Me: You also don't get the full transcript. All right don't get in filters I haven't been getting the full transcript when someone people share things with me.

Them: Huh?

Me: Whereas my notes I get the full transcript so why not just everyone take their own notes? And also I mean. The whole.

Them: Think the purpose is for like let's say you have a like an audience up to write tickets after every stand up so it's more standardized. I think.

Me: Or having six agents debate what the actual answer was might be useful. All right I'm gonna eat before I have to eat in the fucking primary in. You.

Them: Thanks everyone thank you everyone see you later.
