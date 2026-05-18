---
layout: project
title: Channel Performance & Churn Analysis
tagline: "Ten acquisition channels treated as one mix. Split apart, scored on win rate, dialer cost, speed, and retention, the biggest channel was the worst. Synthetic data, real method."
tools: [Python, SQL, Power BI]
outcome_headline: "Five warm channels were 21% of deals but 78% of the revenue that survived the first year, at zero dialer cost"
outcome_detail: "The largest channel by volume won 8.6% of the time, carried 91% of all sales-dialer hours, and kept half its customers. A four-factor scorecard turned that into a scale-cap-kill capacity decision."
order: 2
cover_image: /assets/images/projects/channel-performance-cover.png
github_url: https://github.com/rasmuskampmann1998/rasmus-kampmann-case-studies/tree/main/02-channel-performance-analysis
---

## What this case study demonstrates

A sales team ran ten acquisition channels and reported them as one blended win rate. The blend looked healthy. Underneath it the channels were not one thing: win rates from 4.5% to 79%, time-to-won from a week to a month, and post-sale retention from roughly 50% to 96%. Averaging them hid which channels earned their cost and which burned it.

This is a channel-level analysis with a post-sale axis most channel reporting skips. It asks two questions, not one: which channel wins, and whether the customers it wins stay. The figures here are synthetic, generated from a seeded model that reproduces the shape of a real Pipedrive engagement whose data cannot be published. The method is the point.

Want the schema, the scorecard rule, and the Power BI model: see the [GitHub case study]({{ page.github_url }}).

## Outcome first

One number reframes the whole mix: five warm channels were 21% of deals but 78% of the won revenue still active twelve months later, and they spent zero sales-dialer hours getting it.

The same analysis put cold calling, the single biggest channel, in the cap band. It was 60% of all deals, won 8.6% of the time, consumed 91% of all sales-dialer hours, and kept about half its customers a year out. The deliverable was one additive scorecard a revenue-operations lead can read in two minutes and rerun every quarter from the same tables.

## Context

A team selling into small businesses acquired customers through ten channels: cold calling, LinkedIn outbound, referral, inbound sales, SEO, two paid social channels, cross-sell, upsell, and a re-booking queue for prospects who cancelled a first meeting. Total: 7,300 deals, 1,585 of them won, $1.24M in won monthly recurring revenue.

Capacity planning treated "the channel mix" as a single blended win rate of 21.7%. That number was the problem. It was an average across ten channels that behaved nothing like each other, and it hid the only constraint that actually bound the team: sales-dialer time. Two channels consumed that resource. Both sat near the bottom on every quality measure, and the blend averaged the cost away so nobody could see it.

## The problem

Most teams that run many channels judge them on win rate, blended. Two failures stack on top of each other, and the second one is the expensive one.

The first failure is the average itself. A 21.7% blended win rate is the weighted mean of channels that close at 79% and channels that close at 4.5%. Acting on the average means under-investing in the channels that already work and protecting the ones that do not. The fix for that is simple: stop reporting the blend, report the channels.

The second failure is harder. A channel that wins deals which churn in ninety days is not a good channel, and win rate cannot see that. There was no post-sale view tied back to the channel that acquired the customer, so "good channel" meant "closes deals" and stopped at the contract signature. A channel could look strong on win rate and quietly lose most of that revenue within the year, and the existing reporting would never surface it.

The cost side compounded both failures. Sales-dialer hours, the one finite resource, sat almost entirely on the two channels that returned the least, and the blended report made that invisible too.

The question the analysis had to answer: across all ten channels, which produces the most won revenue fastest, keeps the customers it wins, and where is dialer time being spent that does not come back?

## The approach

Channel is the unit of analysis, not the company and not the rep. Every deal is cut by the channel that acquired it, and every channel is scored on four things, because no single one of them is enough on its own.

**Win rate** is the base rate. Necessary, not sufficient: a channel can win often and still lose money if those wins leave.

**Dialer cost** is the scarce resource. The right efficiency question is won revenue returned per dialer hour, and it only matters for the two channels that spend the resource. Everything else returns revenue at zero dialer cost, which is itself the finding.

**Time-to-won** is a cost in disguise. A channel that closes in a week frees a rep's capacity that a channel taking a month does not. Speed compounds: the faster channel can be worked more times in the same quarter.

**Retention** is the post-sale axis, and it is the one that changed the verdict. Share of won customers still active at twelve months, and net revenue retention, both tied back to the acquiring channel. This is the half of the picture win rate cannot show.

These four collapse into one additive score, then into four action bands: scale, maintain, cap, kill. The score is a rule, not a model, deliberately. A model would be more precise and less useful here, because nobody on the revenue team could audit it or rebuild it next quarter. Every point the rule assigns is traceable to a number in the dimensional tables, and a verification step recomputes the whole thing from the data so the scorecard and the rule that produced it cannot drift apart.

## The findings

**Win rate splits the channels into two populations, and the biggest one is in the wrong half.**

![Win rate by channel]({{ '/assets/images/projects/channel-performance-winrate.png' | relative_url }})
*Win rate per channel, sorted, sales-dialer channels in red. There is no gradient here, there is a cliff. Referral, cross-sell, upsell, inbound, and LinkedIn all clear 61%. Everything else is under 15%. Cold calling, the channel that books the most deals, sits at 8.6%, third from the bottom.*

The win-rate chart is the case for abandoning the blend in one image. The channels do not sit on a smooth curve from good to bad. They form two clusters with nothing in between: five warm channels above 61%, five channels below 15%. A blended average of those two populations describes none of them. Cold calling at 8.6% is not "a bit below average", it is in the bottom cluster, and it is the largest channel the team runs.

**Volume is concentrated exactly where win rate is weakest.**

![Deal volume by channel]({{ '/assets/images/projects/channel-performance-volume.png' | relative_url }})
*Deals created per channel. Cold calling is roughly ten times the next-biggest channel. The single bar that dominates the volume chart is the same channel sitting third from the bottom on win rate.*

Put the two bar charts next to each other and the structural problem is obvious. The channel with the most deals has nearly the worst win rate. The team's capacity was being spent in proportion to volume, and volume was inversely related to quality. This is the dilution trap: a high-volume, low-conversion channel makes the pipeline look busy and the blended number look stable while consuming the capacity that the high-conversion channels needed.

**Retention is a second, independent axis, and it punishes the same channels again.**

![Net revenue retention by channel]({{ '/assets/images/projects/channel-performance-nrr.png' | relative_url }})
*Net revenue retention at twelve months, per channel. Expansion and referral channels keep 87% to 94% of the revenue they win. Cold calling keeps 50%. The dialer channels are red, at the bottom, again.*

This is the chart the original reporting could not produce. Win rate stops at the signature; this starts there. Cold calling wins less often and then loses half of what it does win within a year. Its 23.5% share of won revenue shrinks to 15.7% once churn is taken out. The warm channels are the mirror image: they win more often and the revenue stays. Win rate and retention rank the channels in nearly the same order. On a real dataset, two independent measures agreeing is what tells you the conclusion is not a single-metric artefact; in this synthetic version the agreement is built into the model, so the thing to take from it is the method of checking one axis against a second, not the figures themselves.

**The wins that stay, stay from day one.**

![Logo survival by channel group]({{ '/assets/images/projects/channel-performance-retention-curve.png' | relative_url }})
*Share of won customers still active by month since the deal closed, grouped by channel type. The x-axis is months retained, a real ordered axis. Expansion holds near the top across all twelve months. The outbound dialer line bleeds from the first month and never recovers.*

The survival curve shows the retention gap is not a late-life cliff that better onboarding could fix. The outbound line separates from the others in month one and the gap only widens. When churn starts that early and never recovers, the reading is that the channel is selecting weaker-fit customers rather than serving the same customers worse, which is the difference between "improve retention on this channel" and "stop scaling this channel". On a real dataset that distinction is what the survival shape would tell you; here the shape is generated to demonstrate the method, so treat the conclusion as the method, not as an observed result.

**Speed tells the same story a third time.**

![Time to won by channel]({{ '/assets/images/projects/channel-performance-time-to-won.png' | relative_url }})
*Median and 90th-percentile days from first touch to won, per channel. Expansion closes in under a week at the median. Cold calling takes 20 days, re-bookings 31, with long tails behind both.*

Every axis points the same way. The channels that win more and retain more also close faster, which means they return capacity to the team sooner and can be worked again within the quarter. The channels that win least and churn most are also the slowest, so the same dialer hour buys fewer attempts. There is no axis on which the dialer channels are the better investment.

## The deliverable

The four factors collapse into one additive scorecard. Each channel earns points on win rate, dialer cost, time-to-won, and twelve-month retention, and the total drops it into one of four bands.

- **Scale** (LinkedIn, referral, inbound, cross-sell, upsell): 21% of deals, 69% of won revenue, **78% of the revenue that survived the first year**, 83% retained at twelve months, zero dialer cost. Move budget and capacity here first.
- **Maintain** (Facebook, SEO, Instagram): 14% of deals, 7% of won revenue, mid retention. Hold spend, no new investment.
- **Cap** (cold calling): 60% of deals, 23.5% of won revenue that shrinks to 15.7% net of churn, 91% of dialer hours, 51% retained. It still books real volume, so the call is freeze it, do not grow it. Capping, not killing, because the volume is real even though the quality is not.
- **Kill** (re-bookings): a 4.5% win rate on 312 deals. Stop it as a standalone motion and fold confirmed reschedules back into the channel that originally booked the meeting.

The retention factor is a non-negative bonus by design, not a penalty. Win rate and dialer cost already separate the channels cleanly; retention is there to confirm that split, not to be powerful enough to flip a band on its own. That keeps the rule honest: it cannot be gamed by one strong quarter on a single axis, and a revenue lead can defend every band assignment by pointing at the underlying numbers.

The recommendation was concrete. Move a third of cold-call dialer hours to the warm follow-up motions. Retire the standalone re-booking queue. Rerun the scorecard monthly from the same tables so the bands track reality instead of last quarter's assumptions.

## What I'd do differently

The first pass had no post-sale axis at all. The word "churn" was in the write-up, but it was standing in for "low win rate", which is not churn. A channel that wins and then loses the customer in two months is a different and worse problem than a channel that wins less often, and the analysis could not tell them apart until retention went in. Adding it changed which channels looked safe. A channel can clear a respectable win rate and still belong in the cap band once you can see what happens after the signature. I should have built the post-sale view from the start instead of treating the contract as the finish line.

The smallest channel, re-bookings, has only fourteen won customers. Its retention number is too thin to carry a recommendation, so the kill verdict rests on its 4.5% win rate over 312 deals, not on the fourteen-row retention figure, and it is flagged as small-sample everywhere it appears. A real engagement would run the window longer to give that channel a sample worth a decision rather than a direction.

## Tools

Python with pandas and numpy for the analysis and the verification step. SQL for the schema and the analytical queries, cross-checked in DuckDB. Power BI on a PBIP/TMDL project for the dashboard, validated headless with pbi-cli. Every chart is a bar or a line, one comparison grammar, no second encoding to decode. The whole thing reproduces from one script with no real client data.
