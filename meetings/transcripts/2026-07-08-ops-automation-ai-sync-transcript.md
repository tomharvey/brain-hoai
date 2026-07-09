---
title: Monthly Operations Automation & AI Sync — transcript
meeting: "[[2026-07-08-ops-automation-ai-sync]]"
created: 2026-07-08
type: transcript
---

Them: That's fine. Hey, Tom. Oh, yeah. Hey, Shreya. Hey. You in the office today, Tom? Yeah. I couldn't find it wrong, so we just had to, like, sit somewhere. Yeah. Sorry. That's my bad. I probably not reserved a room for this one. Let me have a look. No, I haven't. I've never reserved a room. I will try and do that next time so that we can be in a room together. Cool. All righty. Well, Jonny was just saying that he's got something to show us today, so I thought we could start with that. And then I wanted to potentially talk about our renewal process is, like, just a brainstorming exercise, see if there's anything we could easily automate. I'd got a few questions for you, Thom, about some of the tools that we use to go through renewal. So, yeah, I'll let Jonny go for first, and then we can just have a bit of a brainstorm about renewables. Sound good? Alrighty. Jonny, over to you and your sunny garden. Cool. It's not that exciting. It's only in the infancy at the moment. It would have been nice if this meeting was next week, to be fair, because it might be a bit more further along the line. But basically, after that session that we had that tom kindly put on a couple of weeks ago where we looked at co-work, I've sort of been using that to chat about automating some stuff for connectivity. There's not really a lot I can show you at the moment. Basically, I've got it to do its first sort of, like, test, and it kind of works. I'm not really going to show you that because it's not perfect. But I'm just going to talk you through the process that I'm automating. And then probably in the next, like, couple of weeks, we'll probably be able to see how. It sort of works. So I'm just going to share the really boring world of my sort of, like, daily jobs. So. Is that sharing? No. That's good. That's good. Let's try again. Why is it gone? No. I just do. Let's try again. It says it sharing, but maybe it's not. Right. So at the moment, basically, I've got this. This spreadsheet and what effectively that'll do is I'll download this every day. From looker into excel. And then. It effectively gives me all the different actions to work off. It's just running slowly for you guys, or is it just my screen? I think it's just your screen. Like, I can hear you fine, but you're completely paused. Okay, fine. I just looked at the screen now. I wasn't doing very much, but you can hear me. Yeah, I can hear you fine. Fine. I'll just talk through really quickly. This has got every single policy on there. It's got all the information about the policy. That get made every day on the policy. So where it's up to, if it's under 75 connected, what I'm working on, I've had a. I've been looking at a few different ways of trying to automate some of this work for a while, but I've always thought it's always fallen down mostly on my own personal preference to use excel rather than Google sheets because I just despise Google sheets. It's horrible. To use daily. So it's kind of always fallen down on that, but then had a little bit of an idea, probably off the back of that coworks. I should have a one. I just asked claud because it's got all these connectors if it can do anything. So I've been having a bit of a chat with the co-work thing. I've been working through it, provisionally started it in that session. And so far, I've built a connector to this sheet, so it can effectively manage the sheet for me. It's able to download the data from Looker, the actual looker look that I use and then do all of the work in the morning. So what I would do is I'll download the new sheet, I'll create a new tab, and then I'll do Vlookups for all of those end columns, pull in all the data from yesterday, you know, all the updates on. And it will also then highlight to me at that point which policies have gone over 35 connects from yesterday, which ones have dropped from yesterday. And all that sort of stuff. So at the moment, in my first test, I've managed to get claud to do all of that for me. So it can access the Excel, it can download the looker file. It can drop it into Excel. It can do the VLOOKUP. It can match everything already used to be. Which is super useful. That saves me about, you know, maybe like 5, 10 minutes a day. And then my next sort of sets of this is there's certain actions that it, that it has on there that you can kind of see, like, it's all in date order. So it'll tell me, like, what's to do today. So if I just filter it by, well, it'll be the ninth now because I've done all the stuff this morning, but I just filter this follow-up column. You'll be able to see that it's got, you know, all the dates that of what he's following up when. So I click on the ninth. This is effectively all the work that I've got to do tomorrow is all of these policies and you'll be able to see that it's got a different. Sort of, like Chase telematics form and those sorts of things. So the next step that I'm going to do is now that it's working and it's able to create me that list every day is I'm going to then use the HubSpot connectors to try and get it to start doing some of this stuff for me in the morning. So where it says Chase telematics form, I'm gonna have to write some stuff that will be able to tell it to go into HubSpot, find the deal for that policy and send the send the reminder Chaser for the telematics form. So that's, that's sort of where, where we're going at the moment. So, yeah, it's very much in its infancy, but that's, that's the general sort of concept. I'll probably then just continue to expand this over the next sort of like couple of months and get it to create the fleet clinic list and all that sort of stuff. Off the back of the sheet, because that's where everything runs from. So, yeah, work in progress. It's not super excited at the minute. It's only basically doing the simple functions. But, yeah, I think over the next few weeks, I'll be adding steps on it as we go. I think. And how did you find it? Like, how did you get it to the point where it was able to pull that data without issue, or is it still in the test phase? Because I, like, as you've been going through this, I've been frantically making notes as to how this relates to what we do for renewals. Like, we have an excel sheet that tracks our renewals, like with the dates and stuff, and then that's what populates deals in HubSpot. So, like, how have you found it pulling the data and, like, getting it right? To be fair, I only have, I only, I've only ran this twice on, on a test, and it worked both times, so, you know, like a problem, I think I had a couple of, like, niggly backs and forth with it, you know, around trying to get the file. Yeah. To store the file. I've had to store the file in the co-work folder within the clawed folder. Because that's, that's the, that's because it's like a local file. So it has to go into there instead. But that doesn't really pose me.

Me: Where did you want to?

Them: To solve a problem personally where it's all right.

Me: Store it? What. Was your initial idea?

Them: So we're trying to store it before you sort of, what was your initial idea of where it's stored? Well, at the moment, I've just got it in my actual documents folder on my desktop. But it didn't like trying to access it from there, then try to do it through one drive, but it also didn't really like that either. So I just thought I want to. I needed to get to a point where I could test that it could do the download. So I just thought, well, I'll just stick it in the co-work folder that it's created because it, it's just going to get me further along. I'd have preferred it somewhere else, like a, you know, one drive or somewhere that's remotely accessible. Just in case. But at the moment, I just didn't the co-work one at the minute. And how have you been finding the access to looker? Because, again, thinking about our renewals, when we create, like, cc's and stuff, we have to use the looker data and that extracts into a CCE template. Shreya, I don't know, actually, before I carry on waffling, have you created a CC generator already?

Me: When we create ICD, we have. A lot data. Yeah. It basically goes into.

Them: Yeah, I've managed to create one where it basically goes into.

Me: Look up, goes into. A.

Them: Lookup. It goes into the CPE information and you just have to give it the client name. I don't know if it downloads it. It just automatically captures the data and then the template that I fill it, it tries to populate that template. Okay. And when you've tested it, how successful has it been?

Me: I don't know if it. Downloads. It. Which is automat. Ically captured. The data. The template that I felt. Populated. Okay. It was. Okay. I have to actually.

Them: It was okay. I actually, like, tweak the presentation a little bit because it was just not taking the right format and stuff. Yeah. Fine, but it does take quite a while because there's a long process to kind of, like, capture the information and stuff like that. But it was actually quite okay. Okay.

Me: Use the right. Format. And the figures. Were fine. It does take. Us to. Because I'm just. Like Jonny.

Them: Because I'm just thinking, like, Jonny, I don't want to overtake yours, like, first. Was there anything else you wanted to talk about in relation to yours? My ideas are just like at the moment, it's so infinite that that was it. Yeah. The concept of it is that I've managed to get it to do the basic functionality of extracting the data and allow me to use Excel, which I'm quite pleased with. And, yeah, it's just now going to be. Adding these bits on or these daily tasks. I probably going to need more help, Tom from you probably when I start talking about HubSpot. Actions and how we can get it to do that, because I found HubSpot.

Me: To get.

Them: To be a little bit of a pain. To get it to do things that, well, in zapier it was. Anyway, on previous experience. So we'll see on that one. But, yeah, at the moment, it seems to be due my at least to do. If it helps, Emily, I just created the look that I actually use. I just gave it the link to looker to that particular look and it just downloaded it without.

Me: Shrey. A.

Them: Andrea, I'm assuming that's what you've done for your CC generator. Like, you've given it the link to the, like CC information page. Yeah, I've moved into my fearless, so I just basically ask you to go into that section of yoga.

Me: So I. M just basically. Asking. That fictional. Okay. Because.

Them: Okay. Nice, because so the, the process that I was talking about earlier is our renewal login process at the moment. We've got it to the point. I believe it's using zapier. Anna created a zap that basically pulls the information from a Excel, well, Google sheets file that the underwriters help populate. It basically tells us which underwriter is going to be working on the renewal, when it's due, six weeks before the renewal, that's when it needs to be logged. So it's got all of, like, the dates and the information in it, and then what it does at the moment, it automatically creates the renewal deal for us in HubSpot, but that's basically it. It doesn't go far enough as to pull the company information. It doesn't pull, like, the winning broker from the previous year. It doesn't, it doesn't, like, populate the, the amount that we expect it to be. Like, we have to go into the portal, into retool, into loads of different other places to pull that information into the deal. So whilst it's good as, like, a starting point, ideally what I would love.

Me: It doesn't. Work. To get to the real.

Them: To get to the point of is that the renewal deal in HubSpot is completely populated with all of the information that we need, so we don't even need to touch that, then what it would do is create the CCE for us so it would go into looker, populate the CCE, generate that for us, both an internal and an external one, because we have to do that. It would then pull those telemetry and speeding reports for us. We wouldn't need to then go and do that. So I'm just thinking, like, Jonny, like, yours is, like, inspired me because I reckon what we could do is get the zappy. Well, we could improve the zapier process so that at least the deal in HubSpot is, is full and we don't need to do anything with it. And that it creates the G drive for us and puts in the field, like the files that we need at least. So that's where my mind is at.

Me: M, then what? Creates a population, both internal analyt. Ical. It would then telemetry that we got to see much more inspiring. Sub. Ject. At least if you're fully. And it creates. With your page. Or.

Them: Tom, do you know how easy it would be for claw to maybe access. Experience? Because we have an experience account where we have to download the, the business file, like the report to make sure that they've not, like, gone into arrears or, like, got ccjs and things like that.

Me: The business. Possible. There is an API for billion. So it's doable.

Them: Possible. There is an API for your premium.

Me: Yeah.

Them: So let's do it again. Okay. Because that's one of the, that's one external source that we need to use experience. Then we've got looker for the Telemetry and critical speeding report and the CCA generation. So that's one connector that we need.

Me: But we've got.

Them: What else? What else? What else? Claims listings? But again, that's fine as well because we get the emails from, like, Andy daily. And we also get the border from Admiral daily. So again, if we can get it so that it searches our emails and downloads the latest file. I, I think that could be doable as well. I just love it to get to the point where pub spot's all done. It's created the ccs for us, it's pulled all of the files and created the g drive. And then all we need to do is really email the broker and then log it on retool or the portal as like a first step, ideally in the future, it would just log it all for us and we wouldn't even need to worry about it. But I think that's probably being a little bit hopeful.

Me: Do you guys have your. Cloud laptop?

Them: You guys have your fair cloth. So I'm currently on the clawed bot, and this afternoon I'm setting up my new laptop with seato. So I've got a new laptop. This is going to be the clawed bot. And what I'll do, I'll probably have a session with you, Tom, once it's set up and we've wiped this one. Set it up and see what we can do with it. Like log it into all of the different systems and stuff with the clawed access and then go from there.

Me: I mean, I'm in the office. Until Friday morning. So.

Them: I mean, I'm in the office until the Friday morning, so. Okay, awesome. I'm in, I'm in tomorrow, so maybe we could grab some time. I'll bring those with me.

Me: One of the things I really like about Jonny. Your approach.

Them: One of the things I really like about Jonny your approach.

Me: You didn't jump to the end. Like you've created this like.

Them: You didn't jump to the end.

Me: Step by step. Building that spreadsheet.

Them: Like, you've created this, like, step by step thing, like building that spreadsheet is like the first step, which is the right way of going about it. And then just when you're talking about all those things, like all of, like, getting into experience to get from A to Z, there's all the letters in between.

Me: First. Step, which is the right way of. Going about it. And Emily, just when you're talking about all. Those things, like all. Like theory. Huge long process. Yeah. From a to Z. We've got that.

Them: Like, if you've got that eject laptop.

Me: For all the experience.

Them: Yeah. For all the experience part of a to Z process.

Me: Like you could extract.

Them: Like you could extract parts of it. So it's, it doesn't have to be done as part of the renewal process, but there's just a process that is spotting ending and HubSpot at least experience data.

Me: The renewal process. But there's just. Experience. In data. And. Adds. It there. So it's there when you need to do. The process.

Them: And it would often get security data as there. So it's there by to do the process. Like processes out and do the, do the very specific experience exploration or other things building owners. Like, it doesn't have to be done as hard on a big process.

Me: Like. Do the. Very specific. Exploration. Or other things. Are.

Them: Yeah. Yeah. I think that's a really good point as well. I think, like you say, like Jonny's sort of started with that process. That's the area that he wants to work on for now. And then he can expand on it. I think for me, because we've got a really clear renewal process document, I think what I'll do is go through it and see which bits could be really easy to automate and just start with those and then bits in between. Okay. Yeah. If we can't automate all of it, that's not a problem. Even if we could just get the HubSpot stuff really clear. So done in the form that we need it. We don't need to touch it. If we can get it to draft the email to the broker and have it, like, populate it and say, here you go, send this amazing the hub spot stuff. I think we could really easily automate. And hopefully the g drive stuff and that would formulate the first basically half of the renewal process and take out a significant chunk of the workload.

Me: Made. Of. Freedom. And. That was basically. Part of the renewal process. Yeah, I guess.

Them: Yeah. Because, yeah, I guess these processes are designed for a person to do and doesn't make sense for some of them to do it until you need to do it.

Me: Doing all that. Free.

Them: Yeah. Doing of it is essentially free. To ornate. Yeah, exactly. Exactly. And the thing is with these renewals as well, like, we sometimes only get, like, one a day, but then yesterday I got four in one day. It's just basically based on when the renewal date fall. So some days we won't have any. Some days in busy periods, we could have, like, five or six. And I'd say on average, they probably take about 20 to 30 minutes to process each. So if you have, like, four in a day, that's already like two hours of work, which is just insane. It's just, it's, it's just very laborious because of how many different steps we have to follow. So, like I said, even if we could just automate the front half of it, that would be super helpful. And the other, the other day, I was playing around with our transfer of agency process. I was talking to Shreya about it the other day because before we again used zapier, which was great to begin with and kind of got us into that, like, automation brain, but it only pulled through, like, one alert. It just says, oh, there's a transfer of agency, and then everything else would be left blank. Whereas what I've done with claud, I now have it so that it will pull all of the information from all over HubSpot.

Me: It will. Draft the temporary.

Them: It will draft a template for me that I can then just immediately post into the transfer of agency channel. It pulls the BDM. It pulls, like, the, the. What do we have to do? We have to check companies house to make sure that the directors are correct and match the document, it pulls up for me. It goes and searches away. So, like, that, again, has just elevated that process. And I feel like if we've been able to do that for the TOA, we can definitely do it for renewals.

Me: Nice. Very cool. I appreciate.

Them: Yeah. I appreciate I've spoken a lot. Freda, anything from you guys. I was just, like, word vomiting, like, just getting all of my ideas out. So I want to give space for other people to talk. I, to be honest, completely agree with everything you said. If we can automate that part of the renewal process, it'd make life so much easier. Yeah. I wonder if we could just put the document we've got into Claude and just say how much of this can you do?

Me: How much this.

Them: Good shout. Just see what it says.

Me: Is.

Them: Yeah. Really good. Chow. Yeah. Yeah. You might be able to do a bit more. Might be able to sweeping it can. I don't know.

Me: Always give it.

Them: Almost give it to say, hey, what's the plan here? What can we automate? What should we tackle first?

Me: Up.

Them: Yeah, we've got the document. We know the process. We can just actually put it in there. Yeah.

Me: Yeah.

Them: That's a good shout.

Me: Anything else?

Them: Yeah. Yeah. Yeah. Anything else that anyone else has been, like, playing around with, experimented with.

Me: No. Not in. My.

Them: No, I'm just going to build on kind of perfect everything that I've been so far, especially with, like, the new business team creator. I want to get into a place where you women can run accurately as much as possible because I feel like when it's really busy, it involves, it kind of has its own mind and kind of skipped success. So I just want to get into a place where maybe I need to add patches or maybe I need to just ask into it 10 at a time or something so that you can actually run properly. So I'm just kind of looking about that so that you can't let you say that one thing. Yeah.

Me: Data. Completely automated. I hear that you guys are going. To circumcise.

Them: I hear that you guys are going to be just biting things of certain sizes.

Me: What was that story, Josh? Are you guys going to be finding policies of certain sizes?

Them: What was that? Sorry, Tom. Are you guys going to be just finding policy of certain sizes?

Me: Yeah. So.

Them: Yeah. So there's the, there's the rumor that we might be starting to look at trade risks. So there's something there that we could have a look at. But that's in the works. It's nothing's decided yet. Okay. We bind. We bind policies like any site. Like, we actually physically bind them, but in terms of, like, pricing them and looking at them, that's with the underwriters at the moment. But there is the potential on the horizon for some authority coming our way. So.

Me: Cool. I guess that would. Impact.

Them: Yeah. Cool. I guess that will impact the need for automation. Yeah, definitely. Yeah. Yeah. I mean, we, we need to do it anyway, purely because of the submission expectations, especially for October, like that, that we saw the. Well, I don't know if you're in the OKR session yesterday, but we saw the, the expectations and the targets. So there's, there's going to be a lot of work coming our way, so we definitely need to get some of this sorted.

Me: So yeah.

Them: Yeah. So, yeah, no, that's everything from me. I was just rambling a little bit, but I definitely feel like that was productive. Yeah. Cool. If anyone thinks of anything, shout me. Tom, I'll, I'll put some time in tomorrow when we're in the office and I'll bring this laptop with me.

Me: I'm going to try.

Them: Yeah. Awesome. All right, guys. Well, thank you. I have an AI workshop for you. You're gonna try. To be honest, if you can get, if you can get Jake on board, he's kind of rallying the troops. So I reference. Yeah, you'll be fine. If anyone wants to come along to that and be like, really, how was it? You guys ultimately in some of this. Yeah, definitely. Yeah. Well, no, I'm around tomorrow, so I'll, I'll put some time in.

Me: Luck. Yeah. I take some boards. But if anyone wants to come on to that and be like, how fun. Ny.

Them: Brilliant. All righty. Thank you, guys.

Me: I think. You should be fine. Early. Curtis is there. I think he'll. Be keen as well. Yeah. The ones are oranges won't show up. To be honest about it. Thank. S.
