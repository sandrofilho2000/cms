export interface iHero {
    id: number,
    name: string,
    title: string,
    text: string,
    highlight_word: string,
    command_line: string
    cta_text: string,
    cta_link: string,
    img: string
}

export interface iStat {
    icon: string
    big_number: string
    title: string
}

export interface iFeature {
    img: string
    title: string
    subtitle: string
    text: string
}

export interface iBanner {
    title: string
    subtitle: string
    cta_text: string
    cta_link: string
}

export interface iFaq {
    title: string
    subtitle: string
    questions: iFaqItem[]
}

export interface iFaqItem {
    question: string
    answer: string
}