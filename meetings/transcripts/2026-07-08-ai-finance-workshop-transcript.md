---
title: AI Finance workshop — transcript
meeting: "[[2026-07-08-ai-finance-workshop]]"
created: 2026-07-08
type: transcript
---

<!-- Raw Granola transcript. Speaker attribution ("Me"/"Them") is unreliable — room mic merged multiple in-room speakers into "Me". Name garblings observed: "Quincy"/"Queen see"/"Punsy"/"Queensy"/"Queen scene"/"Que" → Queency; "Thom" → Tom; "clawed"/"claud"/"cloth"/"Claudia" → Claude; "quad code"/"court code" → Claude Code; "cobalt" → co:work; "next week"/"net sweep"/"nets we"/"Nestvi"/"that suite" → NetSuite; "NTP"/"MTP"/"CP" → MCP; "geordie" → Jordi; "Kevan" → Kevin; "Korsly" → Kirsty; "fable fire" → Fable 5; "look around CP" → Looker MCP; "okls" → OKRs. -->

Me: MCP role open and once that's done code runs a report we could just open my financial controller role and do whatever I do yeah. Matt you're knowing aggressively you run into this rule problem as well. Quite a few of my MCP is just like drop out I was gonna follow that up with like this is because I have the look around CP ever since that one on filed that drops out I also don't know if you ever fixed it or not I never actually tried it after that but whenever I made a dashboard using core to make it in your account yes it would send me the link and say you don't have access I think we changed it so it's not mine but it's still not yours it's just like a generic account yeah but yeah it's the same like data leak but I don't really use that as much anymore.

Them: Would it be better for us to install it again locally? Because. It's not going to make a difference to you? I'm just curious.

Me: Painful process doing the moss installation really.

Them: No, well, the installation wasn't as painful and we had it on everyone's machine locally.

Me: Yeah yeah. When it was on my machine it was really like it was quick yeah to log in all the time and it was in my account.

Them: On his machine locally and he said he still uses it a lot.

Me: Yeah. Yeah could be worth doing I mean I benefit from it at some point or another might as well have it. Yeah that sounds like a good good fix but it says like next week has a problem with users as well I think net suite's more of a next week problem rather than yeah so we're kind of I mean we were a little dubious about just giving clawed the same access to net suite as everyone has because it could just delete everything very quickly by accident so that's why we created that separate role so that role it's view only what can it view is it flock limited or flop premium or both oh I like no idea there were two things Geran be able to answer that for sure. Yeah because I think you'd want to or you could ask it. Yeah because like. What those two would be doing would be sitting on the Flock premium side of next week whereas like Flock limited is our like extra company stuff and I think on you Sarah Jade and maybe Quincy would give a deal when that file so we probably want to have some segregation on that one. Have you guys Jade Quincy Pavel are you guys using the net suite? Integration at all is that useful to you? So far?

Them: I've set it up. I've not been able to use it that much to be honest because I keep getting bugs with it. But I have noticed the same thing with the roles. Where like I'll try and do something and then it won't let me and then I need to like close it all down, open up next week in the MCP role. But Anneliese's point is right about we probably need some. Yeah, although I think everyone's got access to the Flock limited don't they?

Me: Not all of their logins it only works for premium not limited you can in the user settings you can say which files they can see.

Them: Okay yeah that's a fair point.

Me: And usually you've seen bugs other than the login one.

Them: It's just like a mind constantly doesn't connect and then I think I need to just delete it and reinstall it again because it just always comes up like I was looking through it the other day. And what was it yeah I keep saying can't reach next week right now it might need to be reconnected so I just need to. Like try it again. Yeah, I think I had it when I was installing it for first couple of days it got connected but I realized that it gets disconnected as well automatically. So I'm not sure why that happens though. Then I have to reconnect it I mean it's not a huge task but yeah it does get disconnected in between.

Me: Sarah have you used any of these things yet? Well I'm learning how to use it also I'm not sure how I hope I would be I've never used net sweep before a few weeks ago. So once the problems come up I'll definitely tell you. For someone that's not this isn't strictly just a question for you it's maybe a question for the room but like for someone that's never used next week is being able to access it through claud. A good thing like you don't actually have to know how to nan suite works you just need to know in theory you just need to know your like finance question is really unusual so I've always used their own port which is so nice easy so there's. Like just the rewards are just very harms I got sometimes so yeah I think so if I could just ask you a question it'd be so much better. Cool. One thing that comes with like things being more productionized and less playful and experimental is an idea of. Like what the value is I mean I think we discussed when you created your like this helps you work out what it's supposed to do every day so it makes your day much faster. Was there much of a difference between. What you used to have where you had to go get the XL and add it to claude and then run its thing and now it's fully automated because there are much other differences no difference it's just now it runs by itself I don't need to do it maybe I mean I forgot to do it in the morning I would get an answer noise because cloth would run the report based on the folder so if I didn't put the data in the folder I would get a slack message saying hey if I put the data in there now it's yeah I guess it's called the fact that it's fully automated you don't have to do it yourself it's already there. I don't know it gives me more time to think about things I can keep automating because it's about making it simpler right yeah. Cool. Kirsty.

Them: I just wanted to add to that that it definitely does make things a lot smoother one of the things I've discovered since our last session is when creating a skill little trick I've been using is for like the POG reports we have a record of quarter one in 2025 quarter two quarter three each in a column because it's a spreadsheet and I've said to the skill calculate quarter two 2026 which it did brilliantly and then also calculate Q1 2026 and check the values that are in the spreadsheet like so there was a way of just checking that code hadn't gone rogue in that run if that makes sense. So the same calculus was doing for Q2 was applied to Q1 and then checked against the numbers that had been stored there previously that I had checked so it gave me like a sense of I don't need to go through the 64 metrics now and check them. So just a little trick I've been using and it's it's really helped because it flagged one or two places that it had gone a bit off piste. And it just made my time a lot quicker than me having to go through 64 metrics.

Me: Clothesline. Not too much recently one way of saying yes. You wet the interview so yeah I mean Kirsty like is that something you started doing more generally just be like asking it to check its work. Or.

Them: Yeah I've been asking you to check his work where I wanted to share that on this forum because I mean that was something I was sort of grappling with was yeah okay but it's producing numbers now I have to go through 64 metrics and check them all. And so that is a little trick I've been doing and I really sped things up for me and then the other thing is executive summaries so in the skill I've asked it at the end of running to give me an executive summary so it looks at the 64 metrics over the different quarters and any of them that are read in the last quarter it highlights those in this executive summary any of them that have progressively got worse so from you know six quarters ago to now if the numbers got worse it highlights those and then it creates this lovely little summary that I've given to Paul and that's how he's going to run the meeting now instead of them like in the past they used to try to go through the 64 metrics and I feel like they weren't making a lot of traction because there was a lot to discuss Claude has now been able to like extract that and give it to them in a very summarized view so those are two things that I've kind of stumbled across in my experimentation if that's useful to anyone to to to use in their work.

Me: I mean I think we discussed last time Kevan was talking about. Getting it to build Excel files so like not asking Claude to do the calculations but asking it to put the calculations in Excel and then you can you can audit the numbers that it's done. It's debatable how good it is at maths itself so yeah it sounds like that's that's another way of like doing that verification whereas what is really good at is the type of stuff you're talking about there like pulling out executive summaries and insights across 64 metrics and spotting trends and all those kinds of things.

Them: Yeah and I guess you know with the spreadsheet you would if you had the calculations you'd still have to get the data. Dumped there with us where it doesn't you don't have to it's like an extra step missing you don't have to now get the data extract into spreadsheet it finds the spreadsheet in Google drives for me because I've set up that connection it creates another google sheet for me and then I just copy the tab across into the old google sheet it's sort of a safety net that is an overwriting of my previous work. So it's been massive time saver.

Me: Nice.

Them: No formulas needed like it has all that logic in the skill.

Me: Very cool. Matt where'd you go off your sleeve? Short sleeves well most of the finance team I think maybe have seen it. Showed you the AI breakfast I'll just shut my screen so you know that I had this installment schedule that was running and it was cool doing the maths and so often it'd be a so yeah and then I asked you if I could get ew mass access and he said oh I can't remember what you said that ended up getting it asking me and say I didn't listen to you I just took it plug hacked into AWS for you. Know Geran game gets me speaking but anyway I created this was one else there I stole the flock formatting but it essentially is just the installment company so it was a lot of using Claude code your screen. The call and then she. Said. I'm trying to take. It's not like me it's not like me. If we mute the TV.

Them: I can't hear you in the room now.

Me: Can you hear this?

Them: Yes.

Me: Okay Matt you see my screen is off yeah. So yeah I was using. Well I basically got the co-work conversation because I kept it all in one conversation got it just to turn it into one massive MD file prompt and just gave that called code. And I've just been going back and forth between cobalt between code you know it'll spew out this message I'll take this code and say put it in plain English I'll say what I want it into something that Claude can. Very quickly understand and then send that to court code and yeah it's just been making this calculator it's been pretty accurate where does it get the data from? Straight from the data lake? Chris has reviewed all the code and he had one change for me what charter on my code I was using some sort of column I can't remember what the con was he said don't like bother using that because it won't give the allage the correct numbers. After doing that all of the numbers have been correct that I've seen so far and it's just sort of like giving me freedom to you know like add overrides like if there's a different deposit on net suite for whatever reason I'm able to add that there and then from there on all the calculations file off of that same commission. Yeah stuff like one we had recently was a policy that we originally said we can't do call to the MTA turns out we did agree to doing it even though we said no but I was able to add this quarterly MCAs and now it like does calculation perfectly and it spits out schedule that allows you to have these course the MTAs with monthly installments and it's all working in that way. And yeah the other thing is that I got to add something so that it basically audits it every single time so if I go to like. No one Jade today so I went to yesterday's one. First it shows me that like if something's not been mapped correctly whether if it's to Nestvi or to go cardless it tells me. Also do you remember we had a problem with. Like I can't remember if you're in the conversation but I messaged tech saying that there were like a few haulage writers that weren't. Tells me when that happened so I can check that and also it just tells me if there's like something weird used to do this before you had this? I didn't well you just didn't do it I just like took so I'd like download all the MTAs from retool or Queensy wood and we would put them into an excel calculator and hope for the best whereas now it all gets all deserved you know I can see all of the policies here. This has actually helped a bit with broke statements because I can filter per broker that I'm doing. And then check all of their invoices whilst I'm going whereas before I was just like going down the whole list also shows me whenever there's a new business. This one takes months away but yeah when there's a new policy that comes in like the last 24 hours or like I can also choose like a certain inception date and it tells me what was found there. When it comes up here how old have they kickstart in terms of having the first invoices raised do click on it and it will. Tell us through was that more an FYI for you like these yeah it's just more of an FYI it's like if I want to see if there's any policy or something like at the start of the month I'll go in or like the end of the month I'll go in and see how many more I'm going to have on those certain date or something. And but yeah everything flows through automatically I don't have to do anything anymore I don't have to you know scan slack for new policies and add it to my Excel calculator and it's all just sort of. Automatic all I have to do now. And I'm hoping to even automate this as well so is I just have to either download the invoice CSV and credit CSV and then upload it to that suite but with the API key. Which I'm sure one might admins might give me I'll be able to have a button here where I click push and then it goes straight into net suite and I don't have to do anything. I didn't have a question. When you go on holiday someone has to do so you will take leave at some point no actually a desk but how does that work like when you go away can we or access this how we look after it to make sure people still being invoiced not the moment but I'm thinking I might load it onto someone else so it's all in the github at the moment what are you open to the survivor? Yeah this is a web browser that you're opening yeah yeah it's arc what's the URL? It's just a local host yeah it's just all in a private github right now so I would basically just load it onto someone's machine like Queen seats or I don't know whoever wants to do it I'll get it out because it'll be good for a few of us to know how it works so like yeah if you're ever off or busy that someone else can pick it up so much of the work has done in the background now it's mostly someone just in a few buttons but definitely. Run me through this video micronutrient yeah sure yeah sorry yeah.

Them: Is it possible that we could take it from being run on your local machine because you've got it all the code there in github and sort of production it I don't know it's just a question.

Me: Spoke to Geran about this so Jade and I have been talking through okls and what have you and then I showed this at AI breakfast and he had a conversation with me and he was like what's your ideal and I said to have this as an extension of the portal like column pools or something like that and he said we're more likely to take inspiration and I'm perfectly fine with that because this is built around my brain and how I work and he said we need like five year old to be able to use this personally I think I have mental competitor but.

Them: Yeah.

Me: Yeah. That would be the ideal for me but I don't know if that's going to be gonna become a thing I know that a few people in the engineering team are having a look at it I think more for inspiration points. But what I like about it right now is that I can just say it's called I want to add this and then I'll do it and then I have it ready 10 minutes later you know it's for example the Korsly stuff I only added that after Tom briefly mentioned it in a OKR session and I did it during that session and by the end of the session it was there. So yeah.

Them: And does it does it sit okay does it hard code the value so it does a run? Get some from the database stay lake pulls those numbers and then puts them here or is it sitting looking at the database and pulling those numbers in so I miss that part I think you. Maybe like a live view of the data you're going to have to run it and then it gets the numbers right.

Me: It's a. Clue. I run this engine and it does like a few calculations I've already wanted but I haven't like forced run it and it will. Yeah just do a bunch of calculations in the background I think it's a crap in python and then it spews out the numbers and then if I like change a deposit for example like someone has a different deposit in nets we Queen scene I were working on something like that earlier today I do that run the engine again and then it like corrects it all.

Them: In the sort of like. Sort of environment that you've got but not obviously in the database so it corrects it and then create the if it takes your number that you've corrected.

Me: As in. My. Yeah so it's getting the data, it's doing the calculation all of the installment calculation it's views out my numbers here the other thing I didn't mention also like produces a schedule straight away for me and it was links to portal for the brokers to go to the exact dates and everything does it like work for me when we send it outside of Flock you know the other day there was that one and the links so turned up. Wasn't my thing I think that's more that's been a wider because it was also upfront policies. But yeah. So good looks great thanks. So.

Them: Just add to that is that I when I speak to geordie about what the tech and engineering team are doing for the OKR build I think they are very much going to be using this as a basis for what they need. So maybe that wasn't conveyed via Geran but they are they will definitely be using this and especially because you and your role are like the main will be the main user of whatever they produce of the output. So it needs to make sure that it matches here. I think Geran has played around with it as well and come up with like a further version but yeah I think you should definitely take some credit for. And be more than just inspiration for the tech team. They're actually going to be digging into this to see what how it's built.

Me: Yeah I mean that would be. Great if if this was like you know everyone sort of stress tested it made sure everything's running smoothly I mean I've been using it for the past. Month maybe so I feel like any problems that I could have come across I would have come across by now. So far nothing other than the odd one policy and it's that was what Queue and I were working on today and that's because I think next week was wrong for whatever reason so yeah there we go. Thanks. So this is major life. Quicker this is like. Made something that was never possible possible. Yeah like yeah the part that I'm most proud of recently is that like what's the MTA thing because I don't know it's just like. Being able to sort of go back to the broke and be like yeah we can do what you want I'm really happy with which is like basically the whole team So being able to save the sober carrying the finance you can do what you want I mean like I you know this is the point I said earlier about starting to measure like the impact and the you know the outcomes yeah not just like you build up a skill you're using co-work but like being able to tie the outcomes into OKRs is really important. Is honestly phenomenal and that so this was essentially built with fable fire yeah. And that's why I used it was so high last month I got a message from like two days later saying yeah we're going to put you on a premium yeah you get upgraded welcome to the premium lounge but yeah so you know this it's I like how I'm able to just sort of. Hear something from either the finest single one of the other teams and be able to say it's cool we need to have this and it's added. It's like my own personal engineer. Ed sent me Ed sends me. Tweets about AI. As I'm sure he does many people and he's like we should be doing this and I look forward to speaking to ed. In about two hours not not the pop summer festival this to just be like yeah here's Matt and Geran and Chris doing exactly this already awesome. Yeah. So there we are we're better than uber. Which I think we knew anyway. Anyone else got anything any big news about moss things anyone got anything cool about moss? Y line to work.

Them: I think I'd add here because for the month end but especially the reconciliation, I just put the files to Claude and it just lists everything whatever is missing and I've been using it since May but this one was put on it just said each and every entry and just it was very minute difference. So it's really amazing. It saves a lot of time for me in that.

Me: Punsy.

Them: What's that?

Me: Is it kicking the bank creek part of moss? Down. Underneath have we lost everyone?

Them: Time to see the missing again please and yeah I've used in June. It did have references last two months but this month it's just been so accurate. Yeah and another thing I use is I'm pretty sure it makes manager's life easier. I just asked Claude to put direct links for their approvals for each expense and it just gives out all the lists and sends the message to itself. So that is I think probably easier. Approval process for managers.

Me: Oh so is claud then picking up things and sending slack messages to the people that need to follow up nice is it watching for replies to those slacks as well?

Them: I'm not sure about like how but yeah I do get approvals done much quicker than before.

Me: Nice. So. Yeah this is a big big time saver. Like yeah.

Them: Yes.

Me: Awesome. Anyone doing most things a little outside of the monthly end of month thing.

Them: So Kevin's been doing some some really interesting cost analysis stuff for us being able to sort of dig into vendor detail a little bit more which we don't currently have in net suite and that's going to be now used to go to heads of departments and actually talk about their cost versus budget with them. So this is something that we've been crying out for for a very very long time and now with the most integration and claud it just makes it so much easier to do. So that's one way that we're actually going to be really adding some value to the wider business as well through the use of some of these AI tools.

Me: Had asked as we were rolling it out if it was able to get the like the attachments for the expenses which it can so I don't know if anyone's tried this but yeah I mean Que if you're looking at some expense you can actually ask it to give you the PDF. So like one thing that Christian was talking about as a use case for that was like. First for lots of things like for claude for philanthropic like the anthropic bell is just. However many hundreds of thousands of dollars and that's really all you see in moss but like you can actually get the PDF and ask it questions like so get the PDF and tell me how many seats so like how many members of staff are on there so yeah it's able to go a lot deeper and get information from the PDF that's maybe not on the expense. I don't know if anyone's tried that or if that becomes useful for you.

Them: I think that'll be really useful.

Me: Last five minutes anyone got anything they want to show. Or.

Them: I just want to ask with with Moss, we know there was a little bit of back and forth and I try to do an instant I knew that worked and then I learned from Thom that there's a lot of bespokeness to the installation he created. Has everyone managed to get it installed? I don't know we ran into some issues with Anneliese. With the Java with python version and Dave had the same issue. Christian saying to me he doesn't have access and I know I'm going to get him on line when he gets back from holiday and we're going to probably run into the same issue. Is there anyone that can help us with resolving those errors?

Me: Yes I got Dave through it. So.

Them: Brilliant.

Me: I can certainly help anyone that needs it today while I'm in the office but I think it's fairly easy to resolve remotely as well. Now.

Them: Okay, brilliant for Christian would you like to share with me what the fix was around that python version and then I can sit with him. Because I'm pretty sure Jade did you manage to get it installed to the new version? I haven't had a chance to try it yet. Okay do you want me to put five minutes in your diary and I can walk you through it and then I will get this fixed from Thom in case we run into that. Or do you want to have a go at it? Maybe just have a go at it. I'll have a go at it. Yeah, if I get stuck I'll reach out. Okay yeah thank you Thom for resolving that for Dave and grab Thom if you're there in office and he can help you.

Me: Is at the same time I think yeah.

Them: Yeah. Thanks for everyone's patience on that. That was probably one of the most trying things of my life.

Me: I mean Matt you talked about having your tool in quad code. So. Lost everyone again so like if you need to add like quarterly installments you were able to like just get it to code that up yeah so all the files are on my Mac and it has access to all of that in its file and it just makes the changes as it sort of files and then I commit it to GitHub and it goes live. So like the. Moss MTP server similarly lives on github so like if you are or if anyone is using it and runs into like oh. Like the month end report is actually quite a complex thing that you described what has to happen in month end and actually just recorded that in Granola and then say. Go build that. And it went and built the month end thing it also just has like show me this expense and it will go get that expense and like basic building blocks. But yeah if there's other processes that become. Like standard protesters because you now have this extra facility or if there's processes that are a little sticky and need some fixing up. Then we can and Kirsty I think I'd love to get I'd love to get that NTP on your quad code as well. Add features. As they run into them as well.

Them: So I have a question that's not really linked to Moss but one of the things that I use Claude for quite a lot is kind of building dashboards that show me like I don't know answers to different questions or things I'm interested in whether that's like our cash burn and how much money we've got left or like pulling data via looker via the MCP there and looking at like. What. Broker commission as a percentage of GWP is and that type of thing to help kind of drive some business insight. The challenge that I have with Claude is if I have a dashboard that I've created and I want it to be and I schedule it to update really regularly. How can I share that with somebody else to have like constant access to. With a live view of it?

Me: Let me check a distribution because they had the same problem and they were using Google Drive to solve it. So if that's worked for them then. We'll get that working for you guys as well. Is that for life.

Them: Okay but because Claudia creates. Sorry for somebody talking.

Me: That's all right I think that my signal is pretty poor in here but on you good Jade.

Them: Oh it might be mine. And does it because the thing that I like about Claude is how pretty it makes everything look like within itself. What was that sorry?

Me: It'll still be pretty so it's it's basically.

Them: Okay.

Me: It takes it's the same file that you're generating now but instead of storing it on your Mac it stores it on Google Drive and then the whole team shares that Google drive and it automatically downloads that file onto their Macs as well.

Them: The HTML file not an excel file.

Me: Yeah yeah still in HTML it's still HTML still all fine and pretty and clickable.

Them: And it will update every every time that I want it to.

Me: Yeah.

Them: Or will it just push a new file to the same folder?

Me: It could do either yeah. Yeah.

Them: That's helpful. Yes.

Me: Cool.

Them: Yeah.

Me: So I mean I'll help everyone set this up but it's basically. Yeah you point co-work at a folder that's on Google Drive instead of pointing it at your desktop. And then it saves it onto everyone's Mac.

Them: That's fine that sounds simple enough yeah okay thank you.

Me: Anyone else got any questions? Cool. Then thanks everyone. Well done.
