## 2022-06-15 Narrative Stuff
I should make the most of my passion for the narrative project and the stuff I'm about to do with Claire. But at the same time, the project needs more legwork before anything I'll tell her can genuinely stick. I've drafted full proposals along the lines of my idea twice instead of working on it. And that's ignoring the stuff around the Hackathon, my first year project, and every other false start I've pursued with that. Talk is cheap. I shouldn't even have this meeting unless my goal is to listen to her, and I'm already adequately prepared for this meeting.

**What's the goal of my meeting with Claire?** I want to know her angle. What's her approach right now on all this? What about the old projects -- is she still interested in my junk? What about the Coh-Metrix thing? Does she or her advisor have a plan? Does she want to work together on mine?

**What do I want to accomplish?** I should get Semantic CMR working with the data I already have. It doesn't seem to work with the narrative data; I should reproduce Neal's Result on the dataset he used. I'm barely a few steps away from that, and it could even show up in the ICMR paper if I decide it's worth the trouble.

**What would be your first step on this?** I'm...not sure. There's a lot of old work I want to organize first, I guess. If I were beelining, I'd probably redo my SCMR implementation based on my current Clean_CMR implementation. Then I'd fit SCMR to HealyKahana 2005 as before, with semantic operations turned off. Then I'd fit SCMR to HealyKahana 2005 as before, with semantic operations turned on, focused on reproducing Morton & Polyn 2016 Result. If these are the same (even though other aspects of our analysis approaches are different), then I focus on the semantic resonance hypothesis within the same dataset. 

```mermaid
flowchart TD;
Model[[Implement CMR Variants]]
Model1[Base CMR]
Model2[Semantic PCMR]
Model3[/Semantic ICMR/]
New_Model[/Resonant SCMR/]

Fitting[[Fit CMR Variants to Data]]
Baseline[Healy & Kahana, 2015]
Narrative[Cutler et al, 2019]
Novel_Data["Novel Lohnas-Like Dataset(s)"]

Reproduce[[Reproduce Results From Morton & Polyn 2016]]
Result1[Log-Likelihoods] %% slightly better total LL
Result2[CRP by Semantic Similarity] %% CRP as function of semantic similarity
Result3[Persistence of Semantic Organization] %% Semantic organization Score b/t Lags of 2+
Result4[Benchmark Summary Statistics]

Novel1[Semantic Neighbor Contiguity]

Model --> Model1 --> Fitting
Model --> Model2 --> Fitting
Model --> Model3 --> Fitting
Model --> New_Model --> Fitting 
Fitting --> Baseline 
Fitting --> Narrative 
Fitting -.-> Novel_Data
Baseline --> Reproduce 
Novel_Data --> Reproduce 
Narrative --> Reproduce
Novel_Data -.-> Novel1
Reproduce --> Result1 & Result4 & Result2 & Result3 
%% Result1 & Result4 & Result2 & Result3 & Novel1 -.-> Goal1[[Integrated Account of ]]
```

All of this together would validate SCMR as a model of narrative and word list free recall AND test my similarity-driven contextual reinstatement hypothesis across both types of data. But to show that it's a model of _comprehension_, I'd additionally need measurements and analysis from the comprehension literature. So, more data and experiments. 

This is basically an outline of the flow for all my fitting results tied to this project. I can do much of it "now". If it's successful, then I can fake the novel lohnas-like dataset using my different model variants and some arbitrary parameters. For extra credit, I can also perform an extension of the spacing effect analysis. Once I have some predictions about my results, I can implement the experiment and draft the paper.