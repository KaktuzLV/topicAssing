import pandas as pd

dataset = pd.read_csv('preprocessedDescriptions.csv')

dataset['Topic'] = None
dataset['TopicScore'] = None


def assignTopic(text):
    sportKeywords = [
        'football', 'soccer', 'basketball', 'baseball', 'tennis', 'hockey', 'cricket', 'rugby', 'golf',
        'swimming', 'athletics', 'volleyball', 'badminton', 'table tennis', 'cycling', 'wrestling',
        'martial arts', 'gymnastics', 'skiing', 'snowboarding', 'surfing', 'skateboarding', 'track and field',
        'running', 'marathon', 'triathlon', 'formula 1', 'motorsport', 'horse racing', 'polo', 'sailing', 'rowing',
        'canoeing', 'kayaking', 'archery', 'shooting', 'fishing', 'hunting', 'mountaineering', 'climbing', 'hiking',
        'camping', 'yoga', 'pilates', 'aerobics', 'zumba', 'crossfit', 'weightlifting', 'bodybuilding',
        'skateboarding', 'rollerblading', 'ice skating', 'water skiing', 'wakeboarding', 'jet skiing', 'diving',
        'snorkeling', 'windsurfing', 'kiteboarding', 'paragliding', 'bungee jumping', 'skydiving', 'parachuting',
        'rock climbing', 'trail running', 'ultra marathon', 'taekwondo', 'karate', 'judo', 'boxing', 'muay thai',
        'kickboxing', 'fencing', 'cricket', 'baseball', 'softball', 'handball', 'lacrosse', 'american football',
        'rugby league', 'rugby union', 'squash', 'polo', 'bowling', 'billiards', 'snooker', 'curling', 'bobsleigh',
        'luge', 'biathlon', 'cross-country skiing', 'speed skating', 'ice hockey', 'orienteering',
        'pentathlon', 'decathlon', 'archery', 'shooting', 'surfboarding', 'parasailing', 'gymnastics', 'cheerleading',
        'dance', 'figure skating', 'trampoline', 'synchronized swimming', 'powerlifting', 'sumo wrestling', 'wrestling',
        'mountain biking', 'rally racing', 'skateboarding', 'water polo', 'bodyboarding', 'cycling', 'jogging',
        'paddleboarding', 'pole vault', 'long jump', 'high jump', 'shot put', 'discus throw', 'javelin throw',
        'hammer throw', 'sprint', 'hurdles', 'relay race', 'cross country', 'swimming', 'diving', 'synchronized diving',
        'athlete', 'nhl', 'nba', 'ufc', 'league', 'sport'
    ]
    medicineKeywords = [
        'healthcare', 'medical', 'disease', 'doctor', 'patient', 'treatment', 'pharmaceutical', 'vaccine', 'surgery',
        'health', 'hospital', 'nurse', 'medicine', 'clinic', 'emergency', 'diagnosis', 'therapy', 'rehabilitation',
        'pain', 'symptoms', 'cancer', 'cardiology', 'neurology', 'dermatology', 'pediatrics', 'gynecology',
        'obstetrics',
        'radiology', 'pathology', 'psychiatry', 'psychology', 'anatomy', 'physiology', 'pharmacy', 'medical research',
        'medical imaging', 'laboratory', 'clinical trials', 'virology', 'epidemiology', 'public health', 'genetics',
        'immunology', 'microbiology', 'biochemistry', 'pharmacology', 'neurosurgery', 'orthopedics', 'ophthalmology',
        'dentistry', 'endocrinology', 'allergology', 'oncology', 'pulmonology', 'gastroenterology', 'urology',
        'nephrology', 'radiation therapy', 'anesthesiology', 'pathophysiology', 'pain management', 'emergency medicine',
        'forensic medicine', 'geriatrics', 'intensive care', 'cardiovascular', 'respiratory', 'digestive system',
        'nervous system', 'reproductive system', 'immune system', 'endocrine system', 'musculoskeletal system',
        'urinary system', 'visual system', 'mental health', 'holistic medicine', 'alternative medicine',
        'complementary medicine',
        'telemedicine', 'genomic medicine', 'precision medicine', 'health technology', 'medical devices',
        'biotechnology',
        'medical education', 'medical ethics', 'medical breakthrough', 'health policy', 'global health', 'epidemic',
        'pandemic', 'outbreak', 'infectious diseases', 'chronic diseases', 'viral infection', 'bacterial infection',
        'vaccination', 'immunization', 'pharmaceutical industry', 'drug development', 'drug discovery',
        'pharmacotherapy',
        'clinical guidelines', 'medical insurance', 'healthcare system', 'medical records', 'patient care',
        'preventive medicine',
        'diagnostic tests', 'medical equipment', 'medical imaging', 'organ transplant', 'reproductive health',
        'child health',
        'womens health', 'mens health', 'aging population'
    ]
    cultureKeywords = [
        'art', 'music', 'literature', 'film', 'theater', 'dance', 'painting', 'sculpture', 'poetry', 'photography',
        'architecture', 'design', 'museum', 'gallery', 'exhibition', 'performance', 'opera', 'symphony', 'novel',
        'play', 'cinema', 'cinematography', 'documentary', 'animation', 'visual arts', 'contemporary art',
        'classical music',
        'jazz', 'rock', 'pop', 'hip-hop', 'folk music', 'world music', 'singer', 'songwriter', 'composer', 'lyrics',
        'artistic expression', 'creativity', 'art movement', 'art history', 'art criticism', 'artistic techniques',
        'artistic styles', 'artistic genres', 'art education', 'art therapy', 'creative writing', 'storytelling',
        'literary analysis', 'literary criticism', 'literary genres', 'literary period', 'literary theory',
        'literary awards', 'book', 'poem', 'short story', 'drama', 'literary festival', 'literary magazine',
        'literary translation', 'fiction', 'non-fiction', 'biography', 'autobiography', 'photographic art',
        'photography techniques', 'photojournalism', 'portrait', 'landscape photography', 'street photography',
        'documentary photography', 'fine arts photography', 'visual storytelling', 'sculpting techniques', 'ceramics',
        'installation art', 'conceptual art', 'performance art', 'digital art', 'collage', 'calligraphy',
        'graphic design',
        'fashion design', 'interior design', 'architecture styles', 'art cinema', 'experimental film', 'cult film',
        'film festival', 'film production', 'theater genres', 'theater history', 'theatrical performance',
        'stage design',
        'choreography', 'dance styles', 'contemporary dance', 'ballet', 'folk dance', 'street dance',
        'cultural heritage',
        'cultural diversity', 'cultural identity', 'cultural studies', 'pop culture', 'subcultures',
        'cultural movements',
        'cultural criticism', 'cultural exchange', 'cultural impact', 'cultural appreciation', 'cultural events',
        'cultural traditions', 'folklore', 'folk music', 'folk art', 'traditional crafts', 'traditional costumes',
        'oral traditions', 'rituals', 'festivals', 'heritage preservation', 'cultural tourism', 'cultural institutions',
        'museology', 'art market', 'art collectors', 'art auctions', 'art conservation', 'art restoration',
        'music festivals', 'music genres', 'music history', 'music performance', 'music composition', 'music theory',
        'literary festivals', 'literary events', 'literary prizes', 'literary magazines', 'art workshops',
        'art installations', 'art residencies', 'art grants', 'street art', 'public art', 'sound art',
        'street performers',
        'artistic collaborations', 'poetry slams', 'spoken word', 'literary readings', 'film screenings',
        'cultural documentaries',
        'cultural criticism', 'artistic freedom', 'artistic expression', 'creative industries', 'cultural policies',
        'cultural funding', 'art activism', 'cultural entrepreneurship', 'cultural influencers', 'cultural debates',
        'cultural revolution', 'cultural integration', 'cultural anthropology', 'cultural sociology',
        'cultural psychology',
        'cultural geography', 'cultural philosophy', 'cultural ethics'
    ]
    economicsKeywords = [
        'finance', 'economy', 'business', 'investment', 'market', 'stock', 'trade',
        'entrepreneurship', 'employment', 'economic growth', 'macroeconomics', 'microeconomics',
        'banking', 'financial markets', 'economic policy', 'monetary policy', 'fiscal policy',
        'economic indicators', 'economic development', 'economic theory', 'economic systems',
        'economic analysis', 'economic forecasting', 'economic modeling', 'economic inequality',
        'economic crisis', 'economic reform', 'economic globalization', 'economic sanctions',
        'economic incentives', 'economic competition', 'economic equilibrium', 'economic efficiency',
        'economic sectors', 'economic trends', 'economic fluctuations', 'economic cycles',
        'economic integration', 'economic diversification', 'economic empowerment', 'economic stimulus',
        'economic planning', 'economic stability', 'economic indicators', 'economic performance',
        'economic impact', 'economic sustainability', 'economic empowerment', 'economic theory',
        'economic models', 'economic forecasting', 'economic research', 'economic analysis',
        'economic policy', 'economic governance', 'economic reforms', 'economic systems',
        'economic regulation', 'financial management', 'investment strategies', 'financial planning',
        'business management', 'business strategy', 'business development', 'business operations',
        'entrepreneurial skills', 'startups', 'small business', 'corporate finance', 'financial accounting',
        'managerial accounting', 'financial reporting', 'financial analysis', 'capital markets',
        'stock market', 'bond market', 'commodity market', 'foreign exchange market', 'derivatives market',
        'investment banking', 'private equity', 'venture capital', 'mergers and acquisitions',
        'financial risk management', 'financial derivatives', 'risk assessment', 'risk mitigation',
        'financial modeling', 'financial forecasting', 'budgeting', 'taxation', 'public finance',
        'economic planning', 'economic forecasting', 'economic indicators', 'economic growth',
        'economic inequality', 'income distribution', 'poverty', 'unemployment', 'inflation',
        'deflation', 'interest rates', 'exchange rates', 'global trade', 'international finance',
        'international trade', 'economic integration', 'economic sanctions', 'sustainable development',
        'green economy', 'economic incentives', 'economic impact assessment', 'economic evaluation',
        'economic geography', 'regional economics', 'urban economics', 'development economics',
        'environmental economics', 'health economics', 'labor economics', 'industrial economics',
        'transportation economics', 'agricultural economics', 'energy economics', 'behavioral economics',
        'experimental economics', 'game theory', 'economic history', 'economic sociology'
    ]
    scienceKeywords = [
        'science', 'research', 'biology', 'chemistry', 'physics', 'astronomy', 'technology',
        'scientific method', 'experiment', 'data analysis', 'hypothesis', 'theory', 'laboratory',
        'genetics', 'evolution', 'ecology', 'microbiology', 'biochemistry', 'molecular biology',
        'cell biology', 'botany', 'zoology', 'neuroscience', 'physiology', 'anatomy', 'biotechnology',
        'genetic engineering', 'biomedical', 'pharmacology', 'virology', 'immunology', 'epidemiology',
        'climate change', 'environmental science', 'geology', 'meteorology', 'oceanography', 'ecosystems',
        'conservation', 'geography', 'geophysics', 'paleontology', 'archaeology', 'anthropology',
        'astronomical', 'astrophysics', 'cosmology', 'space exploration', 'quantum mechanics',
        'particle physics', 'nuclear physics', 'optics', 'thermodynamics', 'electromagnetism',
        'robotics', 'artificial intelligence', 'computer science', 'data science', 'machine learning',
        'big data', 'algorithm', 'programming', 'software development', 'cybersecurity', 'networks',
        'virtual reality', 'augmented reality', 'nanotechnology', 'materials science', 'engineering',
        'biomechanics', 'civil engineering', 'electrical engineering', 'mechanical engineering',
        'chemical engineering', 'aerospace engineering', 'robotics', 'energy', 'sustainability',
        'neuroscience', 'psychology', 'cognitive science', 'behavioral science', 'social science',
        'economics', 'sociology', 'political science', 'history of science', 'philosophy of science',
        'scientific literacy', 'science communication', 'science education', 'scientific discovery',
        'scientific breakthrough', 'scientific innovation', 'scientific exploration',
        'scientific advancement', 'scientific collaboration', 'scientific ethics',
        'scientific progress', 'scientific community', 'scientific conferences',
        'scientific journals', 'scientific publishing', 'scientific theories',
        'scientific experiments', 'scientific instruments', 'scientific measurements',
        'scientific models', 'scientific simulations', 'scientific data', 'scientific analysis',
        'scientific interpretation', 'scientific validation', 'scientific consensus',
        'scientific skepticism', 'scientific inquiry', 'scientific curiosity', 'scientific curiosity'
    ]
    workKeywords = [
        'job', 'career', 'employment', 'profession', 'occupation', 'workplace', 'employee', 'employer',
        'colleague', 'manager', 'supervisor', 'team', 'office', 'company', 'organization', 'business',
        'workload', 'responsibilities', 'tasks', 'project', 'deadline', 'meeting', 'presentation',
        'collaboration', 'communication', 'leadership', 'management', 'work-life balance', 'flexibility',
        'remote work', 'telecommuting', 'freelancing', 'entrepreneurship', 'startup', 'promotion',
        'salary', 'compensation', 'benefits', 'performance', 'productivity', 'growth', 'learning',
        'development', 'training', 'mentoring', 'networking', 'professionalism', 'workplace culture',
        'diversity', 'inclusion', 'equality', 'workplace ethics', 'workplace well-being',
        'workplace safety', 'stress management', 'time management', 'creativity', 'innovation',
        'problem-solving', 'decision-making', 'critical thinking', 'adaptability', 'resilience',
        'teamwork', 'collaborative', 'autonomous', 'self-motivated', 'goal-oriented', 'efficiency',
        'effectiveness', 'quality', 'workplace satisfaction', 'workplace motivation', 'workplace success',
        'workplace dynamics', 'workplace challenges', 'work-life integration', 'professional growth',
        'career advancement', 'workplace relationships', 'workplace communication', 'workplace conflicts',
        'workplace stress', 'workplace burnout', 'workplace flexibility', 'workplace technology',
        'workplace policies', 'workplace skills', 'workplace learning', 'workplace feedback',
        'workplace performance', 'workplace environment', 'workplace productivity',
        'workplace engagement', 'workplace happiness', 'workplace mindset', 'workplace mindset',
        'workplace resilience', 'workplace well-being programs', 'workplace equality',
        'workplace diversity and inclusion', 'workplace collaboration', 'workplace autonomy'
    ]
    politicalKeywords = [
        'politics', 'government', 'democracy', 'elections', 'politicians', 'political parties', 'legislation',
        'policy', 'governance', 'power', 'public administration', 'public policy', 'constitutions', 'voting',
        'political systems', 'ideology', 'science', 'research', 'campaigns', 'activism', 'reform', 'stability',
        'corruption', 'leaders', 'economy', 'theory', 'discourse', 'sociology', 'participation', 'movements',
        'negotiations', 'representation', 'polarization', 'analysis', 'philosophy', 'rights', 'landscape',
        'history', 'culture', 'engagement', 'decision-making', 'debates', 'journalism', 'behavior', 'influence',
        'alliances', 'accountability', 'reforms', 'institutions', 'unrest', 'leadership', 'will', 'divisions',
        'activism', 'campaigns', 'strategies', 'movements', 'parties', 'rallies', 'debates', 'speeches',
        'propaganda', 'satire', 'lobbying', 'negotiations', 'diplomacy', 'rights', 'freedoms', 'oppression',
        'violence', 'refugees', 'asylum', 'surveys', 'polls', 'consulting', 'endorsements', 'analysis',
        'commentators', 'commentators', 'activism', 'engagement', 'participation', 'donations', 'campaigns',
        'platforms', 'boundaries', 'geography', 'boundaries', 'cartoons', 'art', 'satire', 'humor', 'debates',
        'discourse', 'ideologies', 'leaders', 'ideologies', 'theory'
    ]

    topicScores = {
        'sport': 0,
        'medicine': 0,
        'culture': 0,
        'economics': 0,
        'science': 0,
        'work': 0,
        'political': 0
    }

    # Check for sport topic
    for keyword in sportKeywords:
        if keyword in text:
            topicScores['sport'] += 1

    # Check for medicine topic
    for keyword in medicineKeywords:
        if keyword in text:
            topicScores['medicine'] += 1

    # Check for culture topic
    for keyword in cultureKeywords:
        if keyword in text:
            topicScores['culture'] += 1

    # Check for economics topic
    for keyword in economicsKeywords:
        if keyword in text:
            topicScores['economics'] += 1

    # Check for science topic
    for keyword in scienceKeywords:
        if keyword in text:
            topicScores['science'] += 1

    # Check for work topic
    for keyword in workKeywords:
        if keyword in text:
            topicScores['work'] += 1

    # Check for political topic
    for keyword in politicalKeywords:
        if keyword in text:
            topicScores['political'] += 1

    maxScore = max(topicScores.values())
    mostSuitableTopic = 'other'

    # Get most suitable topic
    if maxScore > 0:
        mostSuitableTopic = max(topicScores, key=topicScores.get)

    return mostSuitableTopic


dataset['Topic'] = dataset['Description'].apply(assignTopic)
topicCounts = dataset['Topic'].value_counts()
print(topicCounts)
preprocessedFile = pd.DataFrame(dataset['Topic'])
preprocessedFile.to_csv('Topic.csv', index=False)
