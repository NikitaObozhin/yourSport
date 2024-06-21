def recomendations_(data):
    
    recom_data = {
        'asten_holer': 'Астеники-холерики: подходят динамичные виды спорта, которые требуют активности и соревновательности, а также быстрой реакции и координации, к примеру, такие как футбол, баскетбол, теннис или бег. Эти виды спорта помогут выплеснуть энергию. ',
        'asten_fleg': 'Астеники-флегматики: предпочитают спокойные и размеренные занятия, средней интенсивности и ритма, которые не требуют слишком большого физического напряжения. Хорошим выбором может стать ходьба, тай-чи, гольф или боулинг. ',
        'asten_sang': 'Астеники-сангвинники: данный тип темперамента характеризуется высокой активностью и энтузиазмом. Рекомендуются виды спорта, которые способствуют социальной активности и командной игре, например, футбол, баскетбол, волейбол, танцы. ',
        'asten_melan': 'Астеники-меланхолики: лучше всего подойдут спокойные и одиночные занятия, которые дополнительно способствуют релаксации и концентрации, такие как йога, плавание, пилатес.',
        
        'normosten_holer': 'Нормостеники-холерики: поскольку холерики обладают энергичным и вспыльчивым темпераментом, им рекомендуется виды спорта, требующие высокой активности и соревновательности, например, футбол, баскетбол, плавание, теннис.',
        'normosten_fleg': 'Нормостеники-флегматики: флегматики, как правило, спокойные и сдержанные люди, поэтому им рекомендуются спортивные занятия, которые могут помочь им разнообразить свою жизнь и повысить энергию. Например, танцы, велосипед, гимнастика или катание на роликах. ',
        'normosten_sang': 'Нормостеники-сангвинники: сангвиники обычно более энергичные и общительные, поэтому им подойдут спортивные виды деятельности, которые позволяют им проявить свою активность и взаимодействие с другими людьми. Это могут быть футбол, баскетбол, волейбол или танцы.',
        'normosten_melan': 'Нормостеники-меланхолики: им рекомендуются спортивные виды деятельности, которые помогают расслабиться, снять стресс и сосредоточиться. К ним относятся йога, плавание, пилатес или гольф.',
        
        'hypersten_holer': 'Гиперстеники-холерики: отлично подойдут индивидуальные и эмоциональные виды спорта, которые помогут выплеснуть энергию, например: бег на короткие дистанции, лёгкая атлетика, борьба, бокс и другие ударные единоборства, фехтование. ',
        'hypersten_fleg': 'Гиперстеники-флегматики обычно спокойные и безмятежные. Они могут наслаждаться спортом, который не требует слишком большой физической активности и конкуренции, средней активности и ритма, например, гольф, боулинг, йога, пилатес, плавание. ',
        'hypersten_sang': 'Гиперстеники-сангвинники обычно энергичны и общительны. Им нравятся активные игры и спортивные виды, которые позволяют им проявить свою социальность и энтузиазм. Отлично для этого подойдут футбол, волейбол, бадминтон, баскетбол, регби.',
        'hypersten_melan': 'Гиперстеники-меланхолики обычно более замкнутые и погруженные в себя. Они часто предпочитают индивидуальные виды спорта, которые могут помочь им сосредоточиться и наладить эмоциональное равновесие, например, плавание, бег, йога, теннис, единоборства. ',
        
    }

    return recom_data[data['morfotype']+'_'+data['psychotype']]