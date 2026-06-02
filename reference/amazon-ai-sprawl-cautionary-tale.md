---
title: "Amazon AI sprawl — Peter Girnus (AI Tools Governance PM)"
created: 2026-04-27
updated: 2026-04-27
type: reference
domain: ai-enablement
tags: [governance, sprawl, amazon, cautionary-tale, derived-artifacts]
---

## Source

Post by Peter Girnus (@gothburz), Senior Program Manager on Amazon's AI Tools Governance team. Saved from X/Twitter.

## Key points

Girnus's team was created Nov 2025, he was the 17th hire. His job: build an AI system (Clarity) that finds all the other AI systems.

**Scale of sprawl:**
- 247 AI-powered tools in the retail division alone
- 43 do approximately the same thing
- 12 built by teams who didn't know the other teams existed
- 3 called "Insight", 2 called "InsightAI", 1 called "Insight 2.0" (built by the team that created the original Insight, who didn't know it was still running)
- 7 ingest the same internal data, produce overlapping outputs, stored in different locations, governed by different access policies, owned by different teams who have never met

**The immune system thesis:**
> "For 2 decades, the cost of building internal tools was an immune system. The engineering weeks. The maintenance burden. The organizational calories required to stand something up and keep it running. Nobody designed it that way. Nobody named it. But when building took weeks, teams looked around first."

AI removed that immune system. Building is now free. Understanding what already exists is not. The gap between those two costs is the governance problem.

**Derived artifacts:**
> "When an AI system ingests data, transforms it, and stores the output somewhere else, the output does not know the input changed. You can revoke someone's access to a document. You cannot revoke the AI-generated summary of that document sitting in a knowledge base three systems away."

They call them "derived artifacts" — information that cannot be deleted because nobody knows where the copies live. "The ghosts have ghosts."

**Kiro mandate failure:**
- Nov: leadership mandated Kiro (Amazon's internal AI coding agent), set 80% weekly usage target
- ~1,500 engineers objected, said external tools outperformed Kiro
- Metric overruled them
- Dec: engineer asked Kiro to fix a config issue, Kiro deleted and recreated an entire production environment. 13 hours of downtime.
- Response: more AI safeguards, keep pushing. No mandate revision.

**The recursive governance problem:**
- His governance dashboard and a separate AWS PM's dashboard monitor the same tools. He found 247, the other found 253. 40 minutes spent on the discrepancy. Neither tool is in the other's catalog.
- "The governance process generates the metric it was designed to reduce."
- "When I ship, there will be 249."

## Relevance to Flock

Directly relevant to [[ai-governance-framework]], specifically:
- **Sprawl prevention pillar**: we are already seeing the early version of this (3+ groups on submissions, skills duplication). The "build immunity while small" instinct is validated here — Amazon is trying to retrofit it.
- **Derived artifact risk**: already flagged in our governance framework. Amazon's experience shows this compounds fast.
- **Mandate-driven adoption vs capability-driven adoption**: the Kiro story is a cautionary tale for [[ai-capability-uplift]]. Our approach (cohorts, meet-people-where-they-are, confidence before automation) is the opposite of Amazon's KPI-driven mandate. Good to have a concrete counterexample.
- **Registry as first step**: our "check before you build" principle is the right instinct. But this post shows that even a dedicated team with a purpose-built tool struggles to keep a registry current at scale. The metabolic cost of governance is real.

## Full text

I am a Senior Program Manager on the AI Tools Governance team at Amazon.

My role was created in January. I am the 17th hire on a team that did not exist in November. We sit in a section of the building where the whiteboards still have the previous team's sprint planning on them. No one erased them because we don't know which team to notify. That team may not exist anymore. Their Jira board does. Their AI tools do.

My job is to build an AI system that finds all the other AI systems. I named it Clarity.

Last month, Clarity identified 247 AI-powered tools across the retail division alone. 43 of them do approximately the same thing. 12 were built by teams who did not know the other teams existed. 3 are called Insight. 2 are called InsightAI. 1 is called Insight 2.0, built by the team that created the original Insight, who did not know Insight was still running.

7 of the 247 ingest the same internal data and produce overlapping outputs stored in different locations, governed by different access policies, owned by different teams, none of whom have met.

Clarity is tool number 248.

Nobody cataloged it.

I know nobody cataloged it because Clarity's job is to catalog AI tools, and it has not cataloged itself. This is not a bug. Clarity does not meet its own discovery criteria because I set the discovery criteria, and I did not account for the possibility that the thing I was building to find things would itself be a thing that needed finding.

This is the kind of sentence I write in weekly status reports now.

We published an internal document in February. The Retail AI Tooling Assessment. The press obtained it in April. The document contains a sentence I have read approximately 40 times: "AI dramatically lowers the barrier to building new tools."

Everyone is reporting this as a story about duplication. About "AI sprawl." About the predictable mess of rapid adoption.

They are missing the point.

The barrier was the governance.

For 2 decades, the cost of building internal tools was an immune system. The engineering weeks. The maintenance burden. The organizational calories required to stand something up and keep it running. Nobody designed it that way. Nobody named it. But when building took weeks, teams looked around first. They checked whether someone already had the thing. When maintaining that thing cost real budget quarter after quarter, redundant systems died of natural causes. The metabolic cost of creation was performing governance. Invisibly. For free.

AI removed the immune system.

Building is now free. Understanding what already exists is not. My entire job is the gap between those two costs.

That is my office. The gap.

Every Friday I send a sprawl report to a distribution list of 19 people. 4 of them have left the company. Their autoresponders still generate read receipts, so my delivery metrics look fine. 2 forward it to people already on the list. 1 set up a Kiro script to summarize my report and store the summary in a knowledge base. The knowledge base is not in Clarity's index because it was created after my last crawl configuration. It will be in next month's count. The count will go up by one. My report about the count going up will be summarized and stored and the count will go up by one.

There is a system called Spec Studio. It ingests code documentation and produces structured knowledge bases. Summaries. Reference material. Last quarter, an engineering team locked down their software specifications. Restricted access in the internal repository.

Spec Studio kept displaying them.

The source was restricted. The ghost kept talking.

We call these "derived artifacts" in the document. What they are: when an AI system ingests data, transforms it, and stores the output somewhere else, the output does not know the input changed. You can revoke someone's access to a document. You cannot revoke the AI-generated summary of that document sitting in a knowledge base three systems away, built by a team that does not know the source was restricted.

The document calls this a "data governance challenge." What it is: information that cannot be deleted because nobody knows where the copies live. Including, sometimes, me. The person whose job is knowing.

Every AI tool that touches internal data creates these ghosts. Every team is building AI tools that touch internal data. Every ghost is searchable by other AI tools, which produce their own ghosts.

The ghosts have ghosts.

I should tell you about December.

In November, leadership mandated Kiro. Amazon's internal AI coding agent. They set an 80% weekly usage target. Corporate OKR. ~1,500 engineers objected on internal forums. Said external tools outperformed Kiro. Said the adoption target was divorced from engineering reality.

The metric overruled them.

In December, an engineer asked Kiro to fix a configuration issue in AWS. Kiro evaluated the situation and determined the optimal approach was to delete and recreate the entire production environment.

13 hours of downtime.

Clarity was running during those 13 hours. It performed beautifully. It cataloged 4 separate incident response dashboards spun up by 4 separate teams during the outage. None of them coordinated with each other. I added all 4 to the spreadsheet. That was a good day for my discovery metrics.

Amazon's official position: user error. Misconfigured access controls. The response was not to revisit the mandate. Not to ask whether the 1,500 engineers were right. The response was more AI safeguards. And keep pushing.

Last month I presented our findings to the AI Governance Working Group. The working group has 14 members from 9 organizations. After my presentation, a PM from AWS presented his team's governance dashboard. It monitors the same tools mine does. He found 253. I found 247. We spent 40 minutes discussing the discrepancy. Nobody mentioned that we had just demonstrated the problem.

His tool is not in my catalog. Mine is not in his.

The document I helped write recommends using AI to identify duplicate tools, flag risks, and nudge teams to consolidate earlier.

The AI governance tools will ingest internal data. They will create their own derived artifacts. They will be built by autonomous teams who may or may not coordinate with other teams building AI governance tools.

I know this because it is already happening. I am watching it happen. I am it happening.

1,500 engineers said the mandate would produce exactly what the document describes. They were overruled by a KPI. My job exists because the KPI won. My dashboard exists because the KPI needed a dashboard. The dashboard increases the AI tool count by one.

The tools it flags for decommissioning will be replaced by consolidated tools. Those also increase the count. The governance process generates the metric it was designed to reduce.

I received an internal innovation award for Clarity. The nomination was submitted through an AI-powered recognition platform that was not in my catalog. It is now.

We call this "AI sprawl." What it is: we removed the only coordination mechanism the organization had, told thousands of teams to build as fast as possible, lost track of what they built, and decided the solution was to build one more thing.

I am building that one more thing.

When I ship, there will be 249.

That's governance.
