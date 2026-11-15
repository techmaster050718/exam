(function () {
  'use strict';
  const { App } = window;
  const root = document.getElementById('ssb-root');

  document.addEventListener('DOMContentLoaded', init);

  function init() {
    App.initTheme();
    const toggle = document.getElementById('theme-toggle');
    toggle.textContent = App.getTheme() === 'dark' ? '☀️' : '🌙';
    toggle.addEventListener('click', () => {
      toggle.textContent = App.toggleTheme() === 'dark' ? '☀️' : '🌙';
    });

    const revisionLink = document.getElementById('revision-link');
    revisionLink.addEventListener('click', (event) => {
      event.preventDefault();
      window.location.assign(revisionLink.href);
    });

    App.applyBranding().then(() => render());
  }

  function render() {
    root.innerHTML = '';

    root.appendChild(hero());
    root.appendChild(summaryStrip());
    root.appendChild(sectionHeader('1. Six-Month SSB Roadmap', 'Month-by-month command plan for the next 180 days'));
    root.appendChild(monthGrid());

    root.appendChild(sectionHeader('2. Lecturette Preparation', 'How to speak confidently, structure answers and avoid memorised delivery'));
    root.appendChild(contentCard(buildLecturetteSections()));

    root.appendChild(sectionHeader('3. Lecturette Master Topics', '50+ preparation topics with practical recall structure'));
    root.appendChild(buildLecturetteBank());

    root.appendChild(sectionHeader('4. Lecturette Topic Difficulty', 'Progression from familiar to abstract and current-affairs-heavy issues'));
    root.appendChild(buildLecturetteDifficulty());

    root.appendChild(sectionHeader('5. Lecturette Practice System', 'A disciplined method to improve clarity, confidence and structure'));
    root.appendChild(buildLecturettePracticeSystem());

    root.appendChild(sectionHeader('6. GD Preparation', 'Group discussion behaviour, entry, logic and leadership'));
    root.appendChild(contentCard(buildGdSections()));

    root.appendChild(sectionHeader('7. GD Speaking Framework', 'Point, reason, example, counter and conclusion'));
    root.appendChild(buildGdFramework());

    root.appendChild(sectionHeader('8. GD Entry Strategies', 'How to enter, support, disagree, correct and summarise without conflict'));
    root.appendChild(contentCard(buildGdEntryStrategies()));

    root.appendChild(sectionHeader('9. GD Mistakes to Avoid', 'Common behaviours that lower group performance'));
    root.appendChild(contentCard(buildGdMistakes()));

    root.appendChild(sectionHeader('10. GD Practice Topics', '40+ broad discussion topics across national, defence, social and technology themes'));
    root.appendChild(buildGdTopics());

    root.appendChild(sectionHeader('11. GD Weekly System', 'A consistent practice cycle for improvement across a month'));
    root.appendChild(buildGdWeeklySystem());

    root.appendChild(sectionHeader('12. Group Tasks and GTO Preparation', 'Planning, leadership, teamwork and task execution'));
    root.appendChild(contentCard(buildGtoSections()));

    root.appendChild(sectionHeader('13. Personal Interview Preparation', 'PIQ, family, education, strengths, weaknesses and motivational dialogue'));
    root.appendChild(contentCard(buildPiSections()));

    root.appendChild(sectionHeader('14. Psychology Preparation', 'TAT, WAT, SRT and SD with realistic follow-up chains'));
    root.appendChild(contentCard(buildPsychologySections()));

    root.appendChild(sectionHeader('15. Communication Development', 'Speaking, vocabulary, confidence and answers without hesitation'));
    root.appendChild(contentCard(buildCommunicationSections()));

    root.appendChild(sectionHeader('16. Current Affairs and Defence Awareness', 'Daily reading, issue framing and command-level preparation'));
    root.appendChild(contentCard(buildCurrentAffairsSections()));

    root.appendChild(sectionHeader('17. Physical and Mental Preparation', 'The discipline needed before the final SSB command'));
    root.appendChild(contentCard(buildPhysicalSections()));

    root.appendChild(sectionHeader('18. Complete SSB Procedure', 'Screening, psychology, GTO, interview and final evaluation'));
    root.appendChild(buildProcedureTimeline());

    root.appendChild(sectionHeader('19. SSB Procedure Quick Map', 'Chronological view of the candidate journey'));
    root.appendChild(buildProcedureMap());

    root.appendChild(sectionHeader('20. Golden Tips and Common Mistakes', 'The habits that improve recommendation chances'));
    root.appendChild(contentCard(buildTipsSections()));

    root.appendChild(sectionHeader('21. Interview, GTO and Psychology Golden Rules', 'Actionable behaviour guidelines across the key stages'));
    root.appendChild(buildGoldenRuleBlocks());

    root.appendChild(sectionHeader('22. Myth vs Reality', 'Correcting common coaching myths and unrealistic expectations'));
    root.appendChild(buildMythVsReality());

    root.appendChild(sectionHeader('23. Final SSB Readiness Checklist', '30-day, 14-day, 7-day, 3-day and 24-hour countdown planning'));
    root.appendChild(contentCard(buildChecklistSections()));

    root.appendChild(sectionHeader('24. Six-Month Progress Tracker', 'Week-wise tracking from week 1 to week 24'));
    root.appendChild(buildProgressTracker());

    root.appendChild(sectionHeader('25. Weekly Minimum Target', 'Recommended baseline for disciplined preparation'));
    root.appendChild(buildWeeklyTarget());

    root.appendChild(sectionHeader('26. Final SSB Readiness Score', 'Self-assessment tool, not a predictor of recommendation'));
    root.appendChild(buildReadinessScore());
  }

  function hero() {
    const wrap = App.el('section', { className: 'hero-card glass' });
    wrap.append(
      App.el('div', { className: 'subject-icon', style: 'font-size:2.2rem;' }, '🎖️'),
      App.el('h1', { style: 'margin:0 0 8px; font-size: clamp(2rem, 4vw, 3.4rem);' }, 'SSB TARGET — NEXT 6 MONTHS'),
      App.el('p', { className: 'text-muted', style: 'font-size:1.02rem; max-width: 900px; margin:0 auto; line-height:1.7;' }, 'A dedicated 6-month SSB command center built for lecturette, GD, GTO, personal interview, psychology, current affairs, communication and final readiness.')
    );
    return wrap;
  }

  function summaryStrip() {
    const stats = [
      ['6', 'Months'],
      ['10', 'Core focus areas'],
      ['1', 'Final SSB command plan'],
      ['100%', 'Preparation discipline']
    ];
    const wrap = App.el('div', { className: 'summary-strip glass' });
    stats.forEach(([value, label]) => {
      wrap.appendChild(App.el('div', { className: 'summary-stat' }, App.el('span', { className: 'summary-stat-value' }, value), App.el('span', { className: 'summary-stat-label' }, label)));
    });
    return wrap;
  }

  function sectionHeader(title, subtitle) {
    const wrap = App.el('div', { className: 'section-header', style: 'margin-top: 2rem;' });
    wrap.append(
      App.el('h2', { className: 'section-title' }, title),
      App.el('span', { className: 'text-muted' }, subtitle)
    );
    return wrap;
  }

  function monthGrid() {
    const months = [
      {
        name: 'Month 1',
        focus: 'Foundation',
        points: [
          'Understand the complete SSB procedure',
          'Improve communication and basic self-introduction',
          'Start newspaper/current affairs reading',
          'Build defence awareness and national issue awareness',
          'Begin speaking practice and lecturette drill',
          'Start basic psychology and GTO understanding'
        ],
        targets: ['3 lecturettes/week', '2 GD practices/week', 'daily speaking practice', 'weekly self-review']
      },
      {
        name: 'Month 2',
        focus: 'Communication + Lecturette',
        points: [
          'Speak without hesitation and structure opinions',
          'Improve confidence, vocabulary and flow',
          'Practice national, defence, social, economic and technological issues',
          'Develop crisp opening and conclusion techniques',
          'Record yourself and remove filler words',
          'Increase lecturette volume and quality'
        ],
        targets: ['4–5 lecturettes/week', '2–3 GDs/week', 'record yourself', 'review fillers and transitions']
      },
      {
        name: 'Month 3',
        focus: 'GD + GTO',
        points: [
          'Practice GD with logical entry, support and contradiction',
          'Focus on listening, teamwork and leadership',
          'Work on group planning, command task understanding',
          'Learn GTO task dynamics and execution mindset',
          'Keep lecturette under time pressure',
          'Build confidence under group observation'
        ],
        targets: ['5 lecturettes/week', '3 GDs/week', '1 GTO cycle/week', 'time-pressured speaking practice']
      },
      {
        name: 'Month 4',
        focus: 'Psychology + PI',
        points: [
          'Train TAT, WAT, SRT and SD with clarity',
          'Prepare PIQ with family, education, hobbies, strengths and weaknesses',
          'Prepare realistic follow-up answers and defence motivation',
          'Practice achievements, failures, responsibilities and goals',
          'Frame why Army / why not police / why not corporate',
          'Prepare for difficult, direct and follow-up questions'
        ],
        targets: ['Psychology practice each week', 'PIQ revision', 'mock interview rounds', 'follow-up chains']
      },
      {
        name: 'Month 5',
        focus: 'Full SSB Simulation',
        points: [
          'Run a weekly mock SSB cycle',
          'Practice screening with confidence and clarity',
          'Simulate psychology, GTO, interview and speaking sessions',
          'Plan one full-day mock cycle every week',
          'Review weak areas from each session',
          'Measure improvement in confidence and consistency'
        ],
        targets: ['Day 1 screening', 'Day 2 psychology', 'Day 3 GTO', 'Day 4 interview', 'Day 5 lecturette + GD', 'Day 6 review']
      },
      {
        name: 'Month 6',
        focus: 'Final Polish',
        points: [
          'Build speed, confidence and consistency',
          'Stay sharp on current affairs and defence awareness',
          'Revise PIQ, lecturette and psychology practice',
          'Refine GTO behaviour and communication',
          'Do full mock SSBs under realistic conditions',
          'Sharpen final presentation and composure'
        ],
        targets: ['30-day countdown', '14-day revision', '7-day revision', '24-hour readiness checklist']
      }
    ];

    const grid = App.el('div', { className: 'subjects-grid' });
    months.forEach((month) => {
      const card = App.el('article', { className: 'glass subject-card', style: 'min-height: 100%;' });
      const heading = App.el('div', { className: 'card-title', style: 'font-size:1.2rem; margin-bottom: 0.6rem;' }, `${month.name} — ${month.focus}`);
      const list = App.el('ul', { style: 'padding-left: 1.1rem; margin: 0.75rem 0 1rem; line-height:1.8;' });
      month.points.forEach((point) => list.appendChild(App.el('li', {}, point)));
      const targets = App.el('div', { className: 'subject-card-stats', style: 'margin-top: 0.25rem;' }, month.targets.join(' • '));
      card.append(heading, list, targets);
      grid.appendChild(card);
    });
    return grid;
  }

  function buildLecturetteSections() {
    return [
      {
        title: 'What lecturette is',
        body: 'Lecturette is a short, structured speech given in front of assessors. It tests confidence, content, structure, clarity, communication and spontaneous thinking.'
      },
      {
        title: 'How it works',
        body: 'The topic is given, you get a few moments to think, and you must speak clearly with a defined opening, body and conclusion.'
      },
      {
        title: 'How to select points',
        body: 'Choose 3–4 logical dimensions, such as Problem → Causes → Impact → Solutions, or History → Present status → Challenges → Way forward.'
      },
      {
        title: 'Structure',
        body: 'Opening: define the topic. Body: use 3–4 dimensions. Conclusion: summarise with a balanced closing. Do not memorise a speech; speak naturally with a framework.'
      },
      {
        title: 'How to handle unknown topics',
        body: 'Use general reasoning, common knowledge and a calm framework. Speak in a structured manner even when the topic is unfamiliar.'
      },
      {
        title: 'Confidence hacks',
        body: 'Pause for one second before starting, keep eye contact, avoid filler words, and use a simple but confident tone.'
      }
    ];
  }

  function buildGdSections() {
    return [
      'Speak only when you have a relevant point; do not interrupt unnecessarily.',
      'Enter logically: start with a point, not chaos.',
      'Listen carefully; build on others instead of dominating.',
      'Support and contradict with rationale, not emotion.',
      'Be cooperative, balanced and respectful in group behaviour.',
      'Leadership means calm direction, not constant talking.'
    ];
  }

  function buildGtoSections() {
    return [
      'Understand group planning tasks, command tasks and complete participation.',
      'Demonstrate initiative, cooperation and discipline.',
      'Treat tasks as a group activity, not a personal performance.',
      'Keep communication clear, structured and team-focused.',
      'Leadership will be judged by how you guide without dominating.'
    ];
  }

  function buildPiSections() {
    return [
      'Prepare PIQ thoroughly: family, hobbies, education, strengths, weaknesses, achievements, failures, responsibilities and goals.',
      'Example: “Why Army?” must be followed by “Why not police?”, “Why not corporate?”, “What do you know about the Army?” and “Which entry are you applying through?”.',
      'Prepare your identity, motivation and service orientation in a realistic manner.',
      'Be ready for direct and follow-up questions without getting defensive.'
    ];
  }

  function buildPsychologySections() {
    return [
      'TAT: narrate a complete scene with characters, emotions, conflict and resolution.',
      'WAT: keep it concise, coherent and action-oriented.',
      'SRT: identify the problem, emotion and likely response in a realistic way.',
      'SD: write with a balanced, thoughtful and grounded approach.',
      'Do not force unrealistic heroism; keep your responses natural and credible.'
    ];
  }

  function buildCommunicationSections() {
    return [
      'Speak without hesitation. A calm tone is more powerful than a rushed one.',
      'Vocabulary matters but clarity matters more than complexity.',
      'Practice opinion formation on defence, economy, social issues, technology and governance.',
      'Focus on opening lines, transitions and conclusions in every answer.'
    ];
  }

  function buildCurrentAffairsSections() {
    return [
      'Read newspaper daily with defence, diplomacy, economy, social and technology focus.',
      'Prepare 2–3 current issues per week for discussion and lecturette practice.',
      'Create basic national issue understanding with an officer-like perspective.',
      'Keep remarks balanced and evidence-based, not emotional or slogan-driven.'
    ];
  }

  function buildPhysicalSections() {
    return [
      'Physical fitness is not a separate task; it is a trust-building requirement.',
      'Work on stamina, running, push-ups, sit-ups and endurance without burnout.',
      'Mental stamina matters just as much: discipline, sleep, consistency and recovery matter.',
      'Prepare to handle pressure with calm body language and positive energy.'
    ];
  }

  function buildProcedureSections() {
    return [
      'Screening: personality, communication, suitability and basic officer-like profile.',
      'Psychology: TAT, WAT, SRT, SD and officer-like thought patterns.',
      'GTO: physical tasks, group tasks, command tasks and team behaviour.',
      'Interview: officer intelligence, emotional stability and motivation.',
      'Final recommendation depends on consistency across all stages, not one single performance.'
    ];
  }

  function buildTipsSections() {
    return [
      'Do not over-memorise; speak naturally and structured.',
      'Do not dominate GDs or become passive; balance confidence with listening.',
      'Do not hide behind generic statements; bring clarity to your views.',
      'Avoid false bravado; real officer-like quality is calm, balanced and purposeful behaviour.'
    ];
  }

  function buildChecklistSections() {
    const blocks = [
      {
        heading: '30-Day Final Countdown',
        items: ['Daily speaking practice', 'Current affairs revision', 'Mock interview and PIQ rehearsal', 'Psychology practice', 'GTO task simulation']
      },
      {
        heading: '14-Day Final Revision',
        items: ['Lecturette preparation', 'GD discussion sets', 'Physical fitness', 'PIQ and defence motivation', 'Self-review notes']
      },
      {
        heading: '7-Day Final Revision',
        items: ['Trim filler words', 'Recheck current affairs', 'Refine opening and conclusion', 'Sleep discipline', 'Calm, confident communication']
      },
      {
        heading: '24-Hour Before SSB Checklist',
        items: ['Prepare documents', 'Review basic facts', 'Sleep well', 'Stay physically fresh', 'Avoid panic and overthinking']
      }
    ];

    const wrapper = App.el('div', { className: 'subjects-grid' });
    blocks.forEach((block) => {
      const card = App.el('article', { className: 'glass subject-card', style: 'min-height: 100%;' });
      const title = App.el('div', { className: 'card-title' }, block.heading);
      const list = App.el('ul', { style: 'padding-left:1.2rem; line-height:1.9; margin: 0.75rem 0 0;' });
      block.items.forEach((item) => list.appendChild(App.el('li', {}, item)));
      card.append(title, list);
      wrapper.appendChild(card);
    });
    return wrapper;
  }

  function buildLecturetteBank() {
    const topics = [
      { title: 'Artificial Intelligence and the Future of Jobs', tags: ['TECHNOLOGY', 'ECONOMY'], points: ['Automation will affect repetitive work first.', 'AI requires reskilling, not just fear.', 'India needs hybrid skill sets in digital and human domains.', 'Education must become future-ready and adaptive.', 'The role of empathy and judgment remains human.'] },
      { title: 'Cyber Warfare and National Security', tags: ['DEFENCE', 'TECHNOLOGY'], points: ['Cyber attacks target infrastructure and data.', 'Modern conflict includes information and digital disruption.', 'National resilience depends on cybersecurity culture.', 'Critical infrastructure needs layered defence.', 'Cyber diplomacy is now a strategic tool.'] },
      { title: 'India’s Role in the Indo-Pacific', tags: ['INTERNATIONAL', 'CURRENT AFFAIRS'], points: ['Shipping lanes and sea routes are strategically vital.', 'India balances security, trade and partnership.', 'Quad and regional cooperation matter.', 'The region faces maritime security challenges.', 'The Indo-Pacific is central to global power dynamics.'] },
      { title: 'India-China Relations', tags: ['INTERNATIONAL', 'DEFENCE'], points: ['Border issues remain sensitive and unresolved.', 'Economic interdependence coexists with strategic rivalry.', 'Dialogue, transparency and stability matter.', 'India seeks a balanced and sovereign foreign policy.', 'Regional peace depends on respect for boundaries.'] },
      { title: 'India-Pakistan Relations', tags: ['INTERNATIONAL', 'DEFENCE'], points: ['Security issues remain central to bilateral ties.', 'Dialogue and trade are constrained by trust deficits.', 'Cross-border terrorism affects stability.', 'Regional peace requires political and diplomatic effort.', 'A constructive approach is necessary for long-term peace.'] },
      { title: 'India’s Defence Modernisation', tags: ['DEFENCE', 'CURRENT AFFAIRS'], points: ['Modernisation focuses on readiness and deterrence.', 'Indigenisation is a strategic priority.', 'Defence production strengthens national security.', 'Technology, training and logistics are crucial.', 'Modern armed forces need speed, agility and adaptability.'] },
      { title: 'Agnipath Scheme', tags: ['DEFENCE', 'SOCIAL'], points: ['It aims to bring short-term recruitment in the armed forces.', 'It seeks to improve youthful energy and operational readiness.', 'Debates centre on continuity, morale and social impact.', 'The scheme needs transparent communication and support.', 'Policy execution matters as much as policy intent.'] },
      { title: 'Women in the Armed Forces', tags: ['SOCIAL', 'DEFENCE'], points: ['Women are contributing across multiple service roles.', 'Operational inclusion needs proper support systems.', 'Training and culture must evolve with capability.', 'Gender participation strengthens national talent pool.', 'Equal opportunity should be matched by proper infrastructure.'] },
      { title: 'Social Media and Youth', tags: ['SOCIAL', 'TECHNOLOGY'], points: ['Social media connects but can distract.', 'It shapes identity, attention and political views.', 'Digital literacy is essential for youth.', 'Real-world discipline matters more than online visibility.', 'Balanced use protects mental health and productivity.'] },
      { title: 'Mental Health Among Youth', tags: ['SOCIAL', 'EDUCATION'], points: ['Academic pressure and uncertainty create stress.', 'Mental wellbeing is a public health priority.', 'Support systems include counseling and family communication.', 'Stigma remains a barrier to treatment.', 'Resilience grows with healthy habits and guidance.'] },
      { title: 'Unemployment in India', tags: ['ECONOMY', 'SOCIAL'], points: ['Structural mismatch affects youth employability.', 'Skilling, apprenticeship and job creation are key.', 'Formal job growth must keep pace with population.', 'Quality employment matters as much as quantity.', 'Education must align with market realities.'] },
      { title: 'Education System in India', tags: ['EDUCATION', 'SOCIAL'], points: ['Access has improved but quality remains uneven.', 'Skill-based learning is crucial for future jobs.', 'Teacher quality and institutional accountability matter.', 'Rural and urban inequalities remain significant.', 'An inclusive system strengthens growth and social mobility.'] },
      { title: 'Uniform Civil Code', tags: ['SOCIAL', 'GOVERNANCE'], points: ['It raises questions of equality and personal law.', 'Legal uniformity can be debated alongside cultural diversity.', 'Implementation requires public consent and sensitivity.', 'Governance must balance rights with social cohesion.', 'The issue is both constitutional and social.'] },
      { title: 'One Nation One Election', tags: ['GOVERNANCE', 'CURRENT AFFAIRS'], points: ['It aims to reduce logistical and fiscal burdens.', 'It can improve policy continuity and electoral efficiency.', 'Federal concerns and state-level autonomy are key issues.', 'Implementation requires constitutional and operational planning.', 'The debate is about governance efficiency and federal balance.'] },
      { title: 'Population Growth and Demographic Dividend', tags: ['SOCIAL', 'ECONOMY'], points: ['India has a large young population.', 'Demographic dividend depends on skill and job creation.', 'Health, education and productivity matter.', 'A young population can be a strength if channelled well.', 'Unplanned growth increases pressure on resources.'] },
      { title: 'Climate Change', tags: ['ENVIRONMENT', 'CURRENT AFFAIRS'], points: ['Climate hazards affect agriculture, health and livelihoods.', 'Mitigation and adaptation both matter.', 'Renewable energy and conservation are urgent.', 'Developing countries need a fair transition path.', 'Climate resilience is a national security issue.'] },
      { title: 'Water Crisis in India', tags: ['ENVIRONMENT', 'GOVERNANCE'], points: ['Groundwater depletion is a major concern.', 'Water governance includes conservation and efficiency.', 'Agriculture remains a major consumer of water.', 'Urban demand and industrial use create stress.', 'Recycling and rainwater harvesting help.'] },
      { title: 'Renewable Energy', tags: ['TECHNOLOGY', 'ENVIRONMENT'], points: ['Solar and wind are central to the transition.', 'Energy security depends on diversification.', 'Storage and grid modernisation remain challenges.', 'India has strong renewable growth potential.', 'Sustainability must be balanced with affordability.'] },
      { title: 'Nuclear Energy in India', tags: ['SCIENCE', 'DEFENCE'], points: ['Nuclear energy contributes to power generation.', 'Safety, regulation and waste management are critical.', 'It is tied to energy security and strategic policy.', 'Public trust depends on transparency and governance.', 'India has balanced civil and strategic nuclear interests.'] },
      { title: 'Space Technology and India', tags: ['SCIENCE', 'TECHNOLOGY'], points: ['Space plays a role in communication, navigation and defence.', 'ISRO has built strong capabilities with cost efficiency.', 'Space contributes to weather, remote sensing and agriculture.', 'Commercial participation is growing.', 'India is expanding strategic space reach.'] },
      { title: 'India’s Digital Economy', tags: ['TECHNOLOGY', 'ECONOMY'], points: ['Digital payments and online services are expanding rapidly.', 'Data and digital infrastructure drive productivity.', 'Cybersecurity and trust remain essential.', 'Digital inclusion can promote social mobility.', 'A digital economy also raises governance challenges.'] },
      { title: 'Cybercrime', tags: ['TECHNOLOGY', 'SECURITY'], points: ['Cybercrime targets identity, finance and privacy.', 'Digital literacy and awareness are key defences.', 'Public institutions need stronger cyber protocols.', 'The cost of cybercrime is economic and social.', 'Prevention requires both technology and awareness.'] },
      { title: 'Terrorism and National Security', tags: ['DEFENCE', 'SECURITY'], points: ['Terrorism challenges internal stability and social cohesion.', 'Counter-terror strategy requires intelligence and resilience.', 'Community trust matters in security operations.', 'Technology helps surveillance but must be balanced with rights.', 'National security needs both force and governance.'] },
      { title: 'Border Security', tags: ['DEFENCE', 'INTERNATIONAL'], points: ['Border security is linked to sovereignty and strategic stability.', 'Technology and infrastructure support border management.', 'Terrain and weather affect operations significantly.', 'Community participation strengthens border security.', 'Strong border management also supports economic development.'] },
      { title: 'Role of Youth in Nation Building', tags: ['SOCIAL', 'GOVERNANCE'], points: ['Youth bring energy, innovation and social participation.', 'Civic awareness matters more than symbolism.', 'Young people can drive local change and public service.', 'Leadership is developed through responsibility and discipline.', 'Nation-building depends on values, not just ambition.'] },
      { title: 'Sports and Youth Development', tags: ['SOCIAL', 'EDUCATION'], points: ['Sports build discipline, leadership and resilience.', 'Physical well-being supports mental health and focus.', 'Sports can improve national pride and social integration.', 'India needs sustained investment in grassroots talent.', 'Sports performance requires structure and long-term planning.'] },
      { title: 'India’s Rise as a Global Power', tags: ['INTERNATIONAL', 'CURRENT AFFAIRS'], points: ['India is becoming more influential in trade and diplomacy.', 'Technology and demographic scale support growth.', 'Global influence depends on strategic stability and trust.', 'India must balance sovereignty with partnership.', 'Strategic autonomy remains an important principle.'] },
      { title: 'Make in India and Defence Production', tags: ['DEFENCE', 'ECONOMY'], points: ['Domestic manufacturing reduces import dependence.', 'Defence industry strengthens strategic autonomy.', 'Innovation and supply-chain depth are essential.', 'Private sector capacity is crucial.', 'Defence production also creates skilled jobs.'] },
      { title: 'AI in Defence', tags: ['DEFENCE', 'TECHNOLOGY'], points: ['AI can support surveillance, analytics and logistics.', 'Human judgment remains essential in combat decisions.', 'Ethical use of AI must be carefully considered.', 'Defence transformation requires trained operators and policy oversight.', 'Technology should strengthen command efficiency, not replace its logic.'] },
      { title: 'Leadership and Discipline', tags: ['ABSTRACT', 'SOCIAL'], points: ['Leadership is about responsibility, not authority alone.', 'Discipline builds consistency and trust in teams.', 'Great leaders create clarity in uncertain situations.', 'Self-control matters as much as public confidence.', 'Leadership quality is visible in crisis response.'] },
      { title: 'Urbanisation and Civic Governance', tags: ['GOVERNANCE', 'SOCIAL'], points: ['Urban growth creates opportunities and strain.', 'Civic systems must adapt to density and migration.', 'Sustainable cities require planning and accountability.', 'Public services define quality of life and trust.', 'Urban governance is a national development issue.'] },
      { title: 'Public Health Infrastructure', tags: ['SOCIAL', 'GOVERNANCE'], points: ['Healthcare quality influences productivity and resilience.', 'Rural access remains uneven and challenging.', 'Digital health can expand coverage if managed well.', 'Prevention and primary care need stronger investment.', 'Public health is an economic issue, not just a services issue.'] },
      { title: 'Women Empowerment and Social Change', tags: ['SOCIAL', 'GOVERNANCE'], points: ['Women’s participation strengthens economic and social outcomes.', 'Education and safety remain critical barriers.', 'Institutional support must be practical and visible.', 'Empowerment is not only about rights but opportunities.', 'Societal transformation needs inclusive policy and culture.'] },
      { title: 'Agriculture and Rural Development', tags: ['ECONOMY', 'SOCIAL'], points: ['Agriculture remains central to livelihoods and food security.', 'Technology, irrigation and market access matter.', 'Rural development needs infrastructure and investment.', 'Farm distress requires structural and policy attention.', 'Sustainable agriculture supports national resilience.'] },
      { title: 'The Future of Work', tags: ['ECONOMY', 'TECHNOLOGY'], points: ['Work patterns are changing due to digitisation.', 'Flexibility and skilling will define employability.', 'Productivity can rise if institutions adapt.', 'Education and workers’ rights need simultaneous focus.', 'Future jobs will combine technical and human competence.'] },
      { title: 'Responsible AI and Ethics', tags: ['TECHNOLOGY', 'ABSTRACT'], points: ['AI needs accountability, fairness and transparency.', 'Bias and data quality affect decisions.', 'Ethics are essential in healthcare, education and security.', 'Public trust requires clear governance.', 'Technology must improve human welfare, not just efficiency.'] },
      { title: 'Climate Adaptation in India', tags: ['ENVIRONMENT', 'GOVERNANCE'], points: ['Adaptation helps protect infrastructure and agriculture.', 'Coastal and mountain regions face unique risks.', 'Resilience planning is a public policy necessity.', 'Local communities need support and information.', 'Adaptation must be practical and region-specific.'] },
      { title: 'Global Supply Chains', tags: ['ECONOMY', 'INTERNATIONAL'], points: ['Supply chains affect trade, manufacturing and resilience.', 'Geopolitics can disrupt logistics and sourcing.', 'India seeks stronger strategic manufacturing capacity.', 'Resilience requires diversification and planning.', 'Supply-chain strategy is now a national priority.'] },
      { title: 'India’s Energy Security', tags: ['ECONOMY', 'TECHNOLOGY'], points: ['Energy demand is rising with growth.', 'Diversifying sources reduces risk.', 'Energy policy affects industry and household welfare.', 'Transition and affordability must be managed together.', 'Energy security influences national stability.'] },
      { title: 'Role of Judiciary in Democracy', tags: ['GOVERNANCE', 'SOCIAL'], points: ['The judiciary protects constitutional values.', 'Timely justice is essential for public trust.', 'Access and accountability remain critical concerns.', 'Judicial independence supports democratic stability.', 'Legal reforms must balance rights and efficiency.'] },
      { title: 'Civic Responsibility and Public Service', tags: ['GOVERNANCE', 'SOCIAL'], points: ['Public service depends on ethical behaviour and accountability.', 'Civic duty is broader than voting.', 'Responsible citizenship supports social trust.', 'Effective institutions need informed citizens.', 'Good governance begins with habits and ethics.'] },
      { title: 'Science and Society', tags: ['SCIENCE', 'SOCIETY'], points: ['Science shapes health, agriculture and industry.', 'Public trust in science is crucial for policy adoption.', 'Scientific literacy strengthens democratic debate.', 'Research funding and innovation matter for long-term growth.', 'Technology can improve life if used wisely.'] },
      { title: 'Role of Media in Democracy', tags: ['CURRENT AFFAIRS', 'SOCIAL'], points: ['Media informs citizens and checks power.', 'Responsible journalism supports accountability.', 'Misinformation weakens public trust and debate.', 'Media literacy is essential in the digital age.', 'A healthy democracy needs both information and scrutiny.'] },
      { title: 'India’s Geopolitical Position', tags: ['INTERNATIONAL', 'DEFENCE'], points: ['India sits at the intersection of major sea and land routes.', 'Strategic autonomy shapes foreign policy choices.', 'Regional partnerships and security architecture matter.', 'Geography has shaped India’s diplomacy and defence planning.', 'India must balance strategic independence with cooperation.'] },
      { title: 'Affordable Healthcare and Diagnostics', tags: ['SOCIAL', 'GOVERNANCE'], points: ['Healthcare access affects both productivity and dignity.', 'Primary and preventive care reduce economic burden.', 'Technology-assisted diagnosis can improve coverage.', 'Public-health policy needs reliable infrastructure.', 'Affordable care is a developmental necessity.'] },
      { title: 'Disaster Management in India', tags: ['GOVERNANCE', 'ENVIRONMENT'], points: ['Disaster preparedness reduces loss of life and property.', 'Urban and coastal risks require planning.', 'Community awareness and early warning systems matter.', 'Coordination among agencies is essential.', 'Resilience is a national requirement.'] },
      { title: 'India’s Administrative Challenges', tags: ['GOVERNANCE', 'SOCIAL'], points: ['Implementation quality often matters more than policy intent.', 'Public administration needs accountability and transparency.', 'Capacity building is crucial for development.', 'State capacity determines service quality.', 'Good governance requires clear systems and ethical leadership.'] },
      { title: 'Future of Defence Technology', tags: ['DEFENCE', 'TECHNOLOGY'], points: ['Defence systems are becoming more tech-intensive.', 'Autonomy, sensing and analytics will shape future force design.', 'Human leadership remains central even in advanced systems.', 'Indigenisation and innovation are strategic priorities.', 'Technology must support readiness and deterrence.'] }
    ];

    const wrap = App.el('div', { className: 'subjects-grid' });
    topics.forEach((topic) => {
      const card = App.el('article', { className: 'glass subject-card', style: 'min-height: 100%;' });
      const title = App.el('div', { className: 'card-title' }, topic.title);
      const tags = App.el('div', { className: 'card-meta', style: 'margin-top: 0.75rem;' });
      topic.tags.forEach((tag) => tags.appendChild(App.el('span', { className: 'meta-chip' }, tag)));
      const list = App.el('ul', { style: 'padding-left: 1.1rem; line-height: 1.8; margin: 0.9rem 0 0;' });
      topic.points.forEach((point) => list.appendChild(App.el('li', {}, point)));
      card.append(title, tags, list);
      wrap.appendChild(card);
    });
    return wrap;
  }

  function buildLecturetteDifficulty() {
    const levels = [
      { title: 'Level 1 — Easy familiar topics', items: ['Education in India', 'Youth and Sports', 'Importance of Discipline', 'Role of Youth in Society'] },
      { title: 'Level 2 — General national topics', items: ['Digital India', 'Water Crisis', 'Unemployment', 'India’s Economy', 'Women Empowerment'] },
      { title: 'Level 3 — Defence/current affairs', items: ['Agnipath Scheme', 'Indo-Pacific Security', 'Border Security', 'Defence Modernisation', 'Cyber Warfare'] },
      { title: 'Level 4 — Complex issues', items: ['Climate Policy', 'AI in Defence', 'Geopolitical Rivalries', 'Global Supply Chains', 'Space Strategy'] },
      { title: 'Level 5 — Abstract/unexpected topics', items: ['Leadership and Discipline', 'Science and Society', 'Civic Responsibility', 'Future of Work', 'Responsible AI'] }
    ];

    const wrap = App.el('div', { className: 'subjects-grid' });
    levels.forEach((level) => {
      const card = App.el('article', { className: 'glass subject-card', style: 'min-height:100%;' });
      const title = App.el('div', { className: 'card-title' }, level.title);
      const list = App.el('ul', { style: 'padding-left: 1.2rem; line-height: 1.9; margin: 0.9rem 0 0;' });
      level.items.forEach((item) => list.appendChild(App.el('li', {}, item)));
      card.append(title, list);
      wrap.appendChild(card);
    });
    return wrap;
  }

  function buildLecturettePracticeSystem() {
    const steps = [
      { title: 'Step 1 — Pick random topic', body: 'Choose a topic outside your comfort zone to improve flexibility.' },
      { title: 'Step 2 — Preparation time', body: 'Take 2–3 minutes to form a simple structure. Do not write a full script.' },
      { title: 'Step 3 — Speak without notes', body: 'Deliver a 2-minute talk on the chosen subject in a natural tone.' },
      { title: 'Step 4 — Record yourself', body: 'Listen to your own speech and identify filler words, repetition and weak transitions.' },
      { title: 'Step 5 — Check delivery quality', body: 'Focus on clarity, confidence, speed, eye contact and conclusion strength.' },
      { title: 'Step 6 — Score out of 10', body: 'Use a simple scorecard: structure, content, confidence, delivery, conclusion.' }
    ];

    const wrap = App.el('div', { className: 'subjects-grid' });
    steps.forEach((step) => {
      const card = App.el('article', { className: 'glass subject-card', style: 'min-height:100%;' });
      card.append(
        App.el('div', { className: 'card-title' }, step.title),
        App.el('p', { className: 'subject-description', style: 'line-height:1.8;' }, step.body)
      );
      wrap.appendChild(card);
    });

    const tracker = App.el('div', { className: 'glass subject-card', style: 'grid-column: 1 / -1; min-height: 100%;' });
    tracker.append(
      App.el('div', { className: 'card-title' }, 'Practice score tracker'),
      App.el('p', { className: 'subject-description', style: 'margin-top: 0.8rem;' }, 'Date • Topic • Structure • Content • Confidence • Delivery • Total')
    );
    wrap.appendChild(tracker);
    return wrap;
  }

  function buildGdFramework() {
    const framework = [
      { title: 'POINT', body: 'State your argument clearly and directly, without vague or long-winded openings.' },
      { title: 'REASON', body: 'Explain why this point matters in the context of the topic and the current situation.' },
      { title: 'EXAMPLE', body: 'Give a crisp fact, real-life instance, or practical example to support the point.' },
      { title: 'COUNTER', body: 'Acknowledge another perspective so your answer appears balanced and mature.' },
      { title: 'CONCLUSION', body: 'End with a forward-looking, balanced direction rather than a rigid or emotional finish.' }
    ];

    const wrap = App.el('div', { className: 'subjects-grid' });
    framework.forEach((item) => {
      const card = App.el('article', { className: 'glass subject-card', style: 'min-height:100%;' });
      card.append(
        App.el('div', { className: 'card-title' }, item.title),
        App.el('p', { className: 'subject-description', style: 'line-height:1.8;' }, item.body)
      );
      wrap.appendChild(card);
    });

    const example = App.el('article', { className: 'glass subject-card', style: 'grid-column: 1 / -1; min-height:100%;' });
    example.append(
      App.el('div', { className: 'card-title' }, 'Example response pattern'),
      App.el('p', { className: 'subject-description', style:'line-height:1.9;' }, '“I agree that social media has educational benefits. However, excessive usage can reduce concentration. A balanced approach is therefore better than rejecting it entirely.”')
    );
    wrap.appendChild(example);
    return wrap;
  }

  function buildGdEntryStrategies() {
    return [
      'First entry: If you know the topic, begin with clarity and one strong point instead of a long opening.',
      'Mid-discussion entry: Wait for a natural pause, then add a relevant angle without interrupting others.',
      'Supporting someone: Build on a teammate’s point with a logical extension, not a separate speech.',
      'Disagreement: Respectfully disagree by giving rationale, evidence or a practical alternative.',
      'Correction: Correct misinformation calmly and factually, without personal attack or aggression.',
      'Bringing silence back: Ask a simple question or give a new direction to restart discussion.',
      'Summarisation: End with a balanced summary that captures key arguments and a practical conclusion.'
    ];
  }

  function buildGdMistakes() {
    return [
      'Shouting or interrupting repeatedly',
      'Speaking without a point or without evidence',
      'Repeating the same argument in a different tone',
      'Monopolising the discussion',
      'Staying silent when you had a valid viewpoint',
      'Using fake aggression or memorised lines',
      'Changing opinion without reason',
      'Trying to impress the assessor instead of contributing meaningfully',
      'Unnecessary statistics without interpretation',
      'Personal attacks instead of argument-based discussion'
    ];
  }

  function buildGdTopics() {
    const topics = [
      { category: 'Defence', title: 'India should increase defence spending or focus on indigenisation?', opening: 'A balanced approach is required because both readiness and affordability matter.' },
      { category: 'Defence', title: 'Will Agnipath change the culture of the armed forces?', opening: 'The scheme can improve youth energy, but continuity and morale need careful management.' },
      { category: 'Defence', title: 'Does cyber warfare matter more than conventional warfare today?', opening: 'Cyber resilience is becoming central to modern security and infrastructure security.' },
      { category: 'Defence', title: 'Should India focus more on jointness among services?', opening: 'Joint operations increase efficiency, coordination and battlefield adaptability.' },
      { category: 'National Issues', title: 'One Nation One Election: Reform or risk?', opening: 'The proposal improves efficiency but must respect federal diversity and constitutional balance.' },
      { category: 'National Issues', title: 'Should India prioritise jobs or skills?', opening: 'Skills and jobs are connected; one without the other creates imbalance.' },
      { category: 'National Issues', title: 'Can India become a developed nation without social inclusion?', opening: 'Inclusive growth is essential for both social stability and economic development.' },
      { category: 'National Issues', title: 'Is national security more important than civil liberties?', opening: 'Security and rights must be balanced through lawful and accountable systems.' },
      { category: 'Social Issues', title: 'Is social media making youth more informed or more distracted?', opening: 'Digital access can help but requires discipline, literacy and balance.' },
      { category: 'Social Issues', title: 'Should censorship increase online to prevent misinformation?', opening: 'Misinformation requires accountability, but censorship must not be arbitrary or suppressive.' },
      { category: 'Social Issues', title: 'Should education focus more on skills than marks?', opening: 'Competency and adaptability are increasingly more valuable than only scores.' },
      { category: 'Social Issues', title: 'Is mental health awareness finally improving in India?', opening: 'A growing conversation is positive, but stigma and support systems still require work.' },
      { category: 'Economy', title: 'Can India sustain high growth without employment quality?', opening: 'Growth is limited if it does not translate into productive jobs and rising incomes.' },
      { category: 'Economy', title: 'Should the country encourage more manufacturing or services?', opening: 'A balanced mix is ideal, but manufacturing strengthens resilience and jobs.' },
      { category: 'Economy', title: 'Is inflation more dangerous than unemployment?', opening: 'Both hurt citizens, but inflation affects purchasing power immediately and broadly.' },
      { category: 'Technology', title: 'Is AI a threat to jobs or an opportunity for productivity?', opening: 'AI can complement human productivity if the transition is managed well.' },
      { category: 'Technology', title: 'Should India regulate AI strictly or allow innovation first?', opening: 'Innovation is important, but responsible governance remains essential.' },
      { category: 'Technology', title: 'Is data privacy more important than convenience?', opening: 'Convenience should not override personal security and autonomy.' },
      { category: 'Technology', title: 'Should India invest more in semiconductor manufacturing?', opening: 'Self-reliance in strategic technologies is becoming essential for national resilience.' },
      { category: 'International Relations', title: 'Should India engage more deeply with the Global South?', opening: 'Development partnerships and shared interests strengthen India’s diplomatic influence.' },
      { category: 'International Relations', title: 'Can strategic autonomy survive in a multipolar world?', opening: 'India can remain independent while also building partnerships and trade ties.' },
      { category: 'International Relations', title: 'Is the Indo-Pacific now the centre of global power?', opening: 'Trade routes, security and energy security make the region central to global strategy.' },
      { category: 'International Relations', title: 'Should India rely more on diplomacy or deterrence?', opening: 'The best strategy combines both: deterrence for security and diplomacy for stability.' },
      { category: 'Environment', title: 'Is India doing enough on climate mitigation?', opening: 'The country is making progress, but the challenge requires both policy and behaviour change.' },
      { category: 'Environment', title: 'Should petrol and diesel vehicles be phased out faster?', opening: 'Transition speed matters, but infrastructure and affordability must be managed carefully.' },
      { category: 'Environment', title: 'Is renewable energy enough to meet India’s future demand?', opening: 'It is essential, but storage, transmission and grid planning must be addressed.' },
      { category: 'Environment', title: 'Should India prioritise water conservation over large-scale projects?', opening: 'Efficiency and conservation often provide faster and more sustainable returns.' },
      { category: 'Youth', title: 'Should youth focus more on public service than private career growth?', opening: 'Public service is valuable, but individual aspiration and national need must be balanced.' },
      { category: 'Youth', title: 'Is entrepreneurship better than a government job for India’s youth?', opening: 'Both have value; the right choice depends on talent, risk tolerance and sector.' },
      { category: 'Youth', title: 'Does the youth of India have enough civic awareness?', opening: 'Awareness is improving, but public responsibility needs stronger everyday practice.' },
      { category: 'Youth', title: 'Should national service become a larger part of youth development?', opening: 'Service experience can build discipline, empathy and responsibility.' },
      { category: 'Abstract', title: 'Does leadership require authority or empathy?', opening: 'Effective leadership relies on both clarity and trust.' },
      { category: 'Abstract', title: 'Is discipline more important than talent?', opening: 'Talent without discipline often remains underutilised, while discipline can multiply ability.' },
      { category: 'Abstract', title: 'Is confidence a personality trait or a skill?', opening: 'Confidence is partly temperament, but it is also built through preparation and practice.' },
      { category: 'Abstract', title: 'Should a nation reward innovation more than tradition?', opening: 'A healthy society needs both innovation and continuity.' },
      { category: 'Current Affairs', title: 'Can India balance economic growth with geopolitical risk?', opening: 'The challenge is to remain stable, competitive and strategically secure at the same time.' },
      { category: 'Current Affairs', title: 'Is international cooperation better than strategic self-reliance?', opening: 'Both are necessary; the right strategy is a balanced one.' },
      { category: 'Current Affairs', title: 'Are digital public platforms a strength or a risk for democracy?', opening: 'They improve access, but governance, privacy and accountability must be strong.' },
      { category: 'Current Affairs', title: 'Can India become a global manufacturing leader?', opening: 'Manufacturing growth requires scale, skill, infrastructure and policy consistency.' },
      { category: 'Current Affairs', title: 'Should India focus more on soft power or hard power?', opening: 'India needs both, but soft power becomes stronger when backed by credibility and capability.' }
    ];

    const wrap = App.el('div', { className: 'subjects-grid' });
    topics.forEach((item) => {
      const card = App.el('article', { className: 'glass subject-card', style: 'min-height:100%;' });
      card.append(
        App.el('div', { className: 'card-title' }, item.title),
        App.el('div', { className: 'meta-chip', style: 'display:inline-flex; margin-top:0.7rem;' }, item.category),
        App.el('p', { className: 'subject-description', style: 'line-height:1.8;' }, item.opening)
      );
      wrap.appendChild(card);
    });
    return wrap;
  }

  function buildGdWeeklySystem() {
    const days = [
      { day: 'Monday', focus: 'Topic research and issue mapping' },
      { day: 'Tuesday', focus: 'Individual speaking practice' },
      { day: 'Wednesday', focus: 'Opposing viewpoint preparation' },
      { day: 'Thursday', focus: 'Timed GD simulation' },
      { day: 'Friday', focus: 'Recorded review and self-correction' },
      { day: 'Saturday', focus: 'Mock GD with peer review' },
      { day: 'Sunday', focus: 'Weakness correction and planning for next cycle' }
    ];

    const wrap = App.el('div', { className: 'subjects-grid' });
    days.forEach((day) => {
      const card = App.el('article', { className: 'glass subject-card', style: 'min-height:100%;' });
      card.append(
        App.el('div', { className: 'card-title' }, day.day),
        App.el('p', { className: 'subject-description', style: 'line-height:1.8;' }, day.focus)
      );
      wrap.appendChild(card);
    });
    return wrap;
  }

  function buildProcedureTimeline() {
    const stages = [
      { title: 'Day 0 / Reporting', body: 'Reporting, documentation, accommodation briefing and joining formalities.' },
      { title: 'Stage I — Screening', body: 'OIR, PPDT, narration, discussion and screening result. Practice clarity, basic reasoning and group communication.' },
      { title: 'Stage II — Psychology', body: 'TAT, WAT, SRT and SD. Focus on realistic, coherent and balanced responses.' },
      { title: 'GTO', body: 'Group discussion, GPE, PGT, HGT, Lecturette, IO, Command Task and Final Group Task.' },
      { title: 'Personal Interview', body: 'PIQ, motivation, background, hobbies, education, family, current affairs and follow-up questions.' },
      { title: 'Conference', body: 'Board evaluation across earlier stages; recommendation is based on overall suitability.' },
      { title: 'Recommendation / Subsequent Process', body: 'Recommended or not recommended depends on overall profile and consistency across the selection process.' }
    ];

    const wrap = App.el('div', { className: 'subjects-grid' });
    stages.forEach((stage) => {
      const card = App.el('article', { className: 'glass subject-card', style: 'min-height:100%;' });
      card.append(
        App.el('div', { className: 'card-title' }, stage.title),
        App.el('p', { className: 'subject-description', style: 'line-height:1.8;' }, stage.body)
      );
      wrap.appendChild(card);
    });
    return wrap;
  }

  function buildProcedureMap() {
    const flow = ['Reporting', 'Screening', 'OIR + PPDT', 'Screening Result', 'Psychology', 'GTO', 'Interview', 'Conference', 'Recommendation', 'Medical / Subsequent Process'];
    const wrap = App.el('div', { className: 'glass subject-card' });
    const text = App.el('p', { className: 'subject-description', style: 'line-height:2; font-size: 0.98rem;' }, flow.join(' ↓ '));
    wrap.append(App.el('div', { className: 'card-title' }, 'SSB Procedure flow'), text);
    return wrap;
  }

  function buildGoldenRuleBlocks() {
    const blocks = [
      { title: 'Interview checklist', items: ['Introduction', 'Family background', 'Academics', 'Friends', 'Hobbies', 'Sports', 'Achievements', 'Failures', 'Strengths', 'Weaknesses', 'Career goals', 'Defence motivation', 'Current affairs', 'Home district and state awareness'] },
      { title: 'GTO golden rules', items: ['Participate actively', 'Cooperate with the group', 'Communicate clearly', 'Take initiative when needed', 'Listen before deciding', 'Stay physically active and calm', 'Do not dominate or disappear'] },
      { title: 'Psychology golden rules', items: ['Be realistic', 'Stay consistent', 'Write practical solutions', 'Avoid artificially heroic stories', 'Be emotionally mature and grounded', 'Do not chase a “magic formula” for TAT stories'] }
    ];

    const wrap = App.el('div', { className: 'subjects-grid' });
    blocks.forEach((block) => {
      const card = App.el('article', { className: 'glass subject-card', style: 'min-height:100%;' });
      const list = App.el('ul', { style: 'padding-left: 1.2rem; line-height: 1.9; margin: 0.75rem 0 0;' });
      block.items.forEach((item) => list.appendChild(App.el('li', {}, item)));
      card.append(App.el('div', { className: 'card-title' }, block.title), list);
      wrap.appendChild(card);
    });
    return wrap;
  }

  function buildMythVsReality() {
    const myths = [
      { myth: 'The loudest candidate gets recommended.', reality: 'Group performance depends on clarity, teamwork, leadership and balance, not volume.' },
      { myth: 'There is a fixed TAT story that guarantees success.', reality: 'Authentic, coherent and believable responses matter more than memorised templates.' },
      { myth: 'You need to know every current affair.', reality: 'Awareness matters, but balanced understanding and articulation are more important than volume.' },
      { myth: 'Only extroverts get recommended.', reality: 'Calm, confident and balanced behaviour matters more than being the most talkative.' },
      { myth: 'One bad task means rejection.', reality: 'SSB is evaluated over the full process; consistency matters more than one moment.' }
    ];

    const wrap = App.el('div', { className: 'subjects-grid' });
    myths.forEach((entry) => {
      const card = App.el('article', { className: 'glass subject-card', style: 'min-height:100%;' });
      card.append(
        App.el('div', { className: 'card-title' }, entry.myth),
        App.el('p', { className: 'subject-description', style: 'line-height:1.8;' }, entry.reality)
      );
      wrap.appendChild(card);
    });
    return wrap;
  }

  function buildProgressTracker() {
    const rows = [];
    for (let week = 1; week <= 24; week++) {
      rows.push({
        month: `Week ${week}`,
        lecturettes: Math.max(2, Math.min(5, week % 5 + 2)),
        gds: week % 3 === 0 ? 3 : 2,
        mockInterviews: week % 4 === 0 ? 1 : 0,
        psychology: week % 2 === 0 ? 2 : 1,
        gto: week % 6 === 0 ? 1 : 0,
        currentAffairs: 'Daily',
        weakness: 'Review',
        target: 'Improve clarity and confidence',
        score: '—'
      });
    }

    const tableWrap = App.el('div', { className: 'glass subject-card' });
    const table = App.el('table', { style: 'width:100%; border-collapse: collapse; font-size: 0.85rem;' });
    const thead = App.el('thead');
    thead.appendChild(App.el('tr', {},
      App.el('th', { style: 'text-align:left; padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, 'Week'),
      App.el('th', { style: 'text-align:left; padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, 'Lecturettes'),
      App.el('th', { style: 'text-align:left; padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, 'GDs'),
      App.el('th', { style: 'text-align:left; padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, 'Mock PI'),
      App.el('th', { style: 'text-align:left; padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, 'Psychology'),
      App.el('th', { style: 'text-align:left; padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, 'GTO'),
      App.el('th', { style: 'text-align:left; padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, 'Current Affairs')
    ));
    table.appendChild(thead);
    const tbody = App.el('tbody');
    rows.forEach((row) => {
      const tr = App.el('tr');
      tr.append(
        App.el('td', { style: 'padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, row.month),
        App.el('td', { style: 'padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, row.lecturettes),
        App.el('td', { style: 'padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, row.gds),
        App.el('td', { style: 'padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, row.mockInterviews),
        App.el('td', { style: 'padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, row.psychology),
        App.el('td', { style: 'padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, row.gto),
        App.el('td', { style: 'padding:8px; border-bottom:1px solid rgba(255,255,255,0.15);' }, row.currentAffairs)
      );
      tbody.appendChild(tr);
    });
    table.appendChild(tbody);
    tableWrap.appendChild(table);
    return tableWrap;
  }

  function buildWeeklyTarget() {
    const items = [
      '3–5 lecturettes per week',
      '2–3 GD practices per week',
      '1 mock interview per week',
      '2 psychology practice sessions per week',
      '1 GTO-focused practice per week',
      'Daily current affairs revision',
      '1 self-review session every week'
    ];

    const wrap = App.el('div', { className: 'glass subject-card' });
    const list = App.el('ul', { style: 'padding-left:1.2rem; line-height:2.1; margin:0.75rem 0 0;' });
    items.forEach((item) => list.appendChild(App.el('li', {}, item)));
    wrap.append(App.el('div', { className: 'card-title' }, 'Recommended weekly baseline'), list);
    return wrap;
  }

  function buildReadinessScore() {
    const metrics = [
      'Communication', 'Lecturette', 'GD', 'Interview', 'Psychology', 'GTO', 'Current Affairs', 'Defence Awareness', 'Self-Awareness', 'Confidence'
    ];
    const wrapper = App.el('div', { className: 'glass subject-card' });
    const list = App.el('ul', { style: 'padding-left:1.2rem; line-height:2.2; margin:0.75rem 0 0;' });
    metrics.forEach((metric) => {
      list.appendChild(App.el('li', {}, `${metric}: /10`));
    });
    wrapper.append(
      App.el('div', { className: 'card-title' }, 'Self-assessment scorecard'),
      App.el('p', { className: 'subject-description', style: 'margin-top:0.7rem;' }, 'Overall SSB Preparation Score = sum of all 10 metrics ÷ 10. This is a self-assessment tool only, not a predictor of recommendation.'),
      list
    );
    return wrapper;
  }

  function contentCard(items) {
    const wrap = App.el('div', { className: 'subjects-grid' });
    const array = Array.isArray(items) ? items : [];

    if (array.length && typeof array[0] === 'object') {
      array.forEach((item) => {
        const card = App.el('article', { className: 'glass subject-card', style: 'min-height:100%;' });
        card.append(
          App.el('div', { className: 'card-title' }, item.title),
          App.el('p', { className: 'subject-description', style: 'line-height:1.8;' }, item.body)
        );
        wrap.appendChild(card);
      });
      return wrap;
    }

    const card = App.el('article', { className: 'glass subject-card', style: 'min-height:100%;' });
    const list = App.el('ul', { style: 'padding-left:1.2rem; line-height:1.9; margin:0.25rem 0 0;' });
    array.forEach((item) => list.appendChild(App.el('li', {}, item)));
    card.append(list);
    wrap.appendChild(card);
    return wrap;
  }
})();
