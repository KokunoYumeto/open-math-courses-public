"""Produce complete standalone editable TeX editions; no engine is launched."""
import hashlib,json,math,re,shutil,subprocess,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf8')
out=Path(__file__).resolve().parent
pandoc=shutil.which('pandoc')
if not pandoc:raise RuntimeError('Pandoc is required for Markdown-to-TeX conversion')
base='https://kokunoyumeto.github.io/open-math-courses/courses/AG-RG/'

def figure_tex():
    lines=[r'\begin{center}',r'\begin{tikzpicture}[x=.94cm,y=.94cm,>=stealth,font=\small]']
    systems=[('A_2',(-.5,math.sqrt(3)/2),[(1,0),(0,1),(1,1)],30),
             ('B_2',(-1.,1.),[(1,0),(0,1),(1,1),(2,1)],45),
             ('G_2',(-1.5,math.sqrt(3)/2),[(1,0),(0,1),(1,1),(2,1),(3,1),(3,2)],60)]
    for j,(name,beta,pairs,start) in enumerate(systems):
        roots=[(i+k*beta[0],k*beta[1]) for i,k in pairs]
        for row in range(2):
            vectors=roots if row==0 else [(2*x/(x*x+y*y),2*y/(x*x+y*y)) for x,y in roots]
            lines.append(r'\begin{scope}[shift={('+f'{5.2*j:.1f},{-5.6*row:.1f}'+r')}]')
            lines.append(r'\path[fill=green!12] (0,0) -- ('+f'{start}:2.35'+r') arc ('+f'{start}:90:2.35'+r') -- cycle;')
            for x,y in vectors:
                length=math.hypot(x,y); a,b=-y/length*2.35,x/length*2.35
                lines.append(r'\draw[gray!25] ('+f'{a:.9f},{b:.9f}'+') -- ('+f'{-a:.9f},{-b:.9f}'+');')
            for k,(x,y) in enumerate(vectors):
                colour=['red!70!black','blue!70!black'][k] if k<2 else 'orange!85!black'
                lines.append(r'\draw[->,gray,line width=.55pt] (0,0) -- ('+f'{-x:.9f},{-y:.9f}'+');')
                lines.append(r'\draw[->,'+colour+r',line width=.7pt] (0,0) -- ('+f'{x:.9f},{y:.9f}'+');')
                if k<2:
                    label=[r'\alpha',r'\beta'][k]+(r'^\vee' if row else '')
                    lines.append(r'\node[text='+colour+'] at ('+f'{x*1.12:.9f},{y*1.12:.9f}'+') {$'+label+'$};')
            lines.extend([r'\fill (0,0) circle (.035);',
                r'\draw[gray] (.8,-2.1) -- (1.8,-2.1);',
                r'\node[font=\scriptsize,text=gray] at (1.3,-2.28) {1 unit};',
                r'\node at (0,2.65) {$'+name+r'$ '+('roots' if row==0 else 'coroots')+'};',r'\end{scope}'])
    return '\n'.join(lines+[r'\end{tikzpicture}',r'\end{center}'])

preamble=r'''\documentclass[11pt,a4paper,openany]{report}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=23mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{longtable,booktabs,array,calc}
\newcounter{none}
\usepackage{graphicx,xcolor,tikz}
\usepackage{microtype}
\usepackage[unicode,breaklinks,colorlinks,linkcolor=blue!45!black,urlcolor=blue!45!black]{hyperref}
\urlstyle{same}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\passthrough}[1]{#1}
\providecommand{\NL}{\operatorname{NL}}
\providecommand{\colim}{\operatorname*{colim}}
\setlength{\parindent}{0pt}
\setlength{\parskip}{.4em}
\setlength{\emergencystretch}{3em}
\setcounter{tocdepth}{1}
\setcounter{secnumdepth}{0}
\renewcommand{\chaptername}{Lesson}
\DeclareUnicodeCharacter{03BB}{\ensuremath{\lambda}}
\DeclareUnicodeCharacter{0393}{\ensuremath{\Gamma}}
\DeclareUnicodeCharacter{2192}{\ensuremath{\rightarrow}}
\DeclareUnicodeCharacter{2011}{-}
\DeclareUnicodeCharacter{202F}{\,}
\DeclareUnicodeCharacter{2212}{\ensuremath{-}}
\DeclareUnicodeCharacter{03B1}{\ensuremath{\alpha}}
\DeclareUnicodeCharacter{03B2}{\ensuremath{\beta}}
\DeclareUnicodeCharacter{03BC}{\ensuremath{\mu}}
\DeclareUnicodeCharacter{03A6}{\ensuremath{\Phi}}
\DeclareUnicodeCharacter{2260}{\ensuremath{\ne}}
\DeclareUnicodeCharacter{00D7}{\ensuremath{\times}}
\DeclareUnicodeCharacter{2082}{\ensuremath{_2}}
\DeclareUnicodeCharacter{2228}{\ensuremath{\vee}}
\DeclareUnicodeCharacter{2032}{\ensuremath{^{\prime}}}
\DeclareUnicodeCharacter{220E}{\ensuremath{\square}}
'''

def convert(text):
    text=re.sub(r'<a id="([^"]+)"></a>',lambda m:r'\phantomsection\label{'+m[1]+'}',text)
    text=re.sub(r'\]\((AG-RG-[A-Za-z0-9-]+)\.md([^)]*)\)',lambda m:']('+base+m[1]+'.html'+m[2]+')',text)
    text=re.sub(r'!\[Roots and coroots[^\n]*\n',lambda m:figure_tex()+'\n',text)
    result=subprocess.run([str(pandoc),'-f','markdown+tex_math_dollars+tex_math_single_backslash+pipe_tables+raw_tex',
                           '-t','latex','--top-level-division=chapter','--wrap=none'],
                           input=text,text=True,encoding='utf8',capture_output=True,check=True)
    if result.stderr:print(result.stderr.strip())
    # Keep a theorem's attribution paragraph with the start of its statement.
    # Section headings already prohibit a break before the attribution.
    converted=re.sub(r'(\\emph\{Adapted from the Stacks project,[^\n]*\}\n)\n',
                     lambda m:m[1]+r'\nopagebreak[4]'+'\n\n',result.stdout)
    # These paragraphs can acquire an invalid glyph offset from font expansion
    # in the collected edition. Keep its exact text and use ordinary spacing.
    converted=re.sub(r'^((?:For completeness, this list follows from the reflection axioms,|Over [^\n]+?, it is useful initially to allow a smooth affine monomorphism)[^\n]+)$',
                     lambda m:r'\begingroup\microtypesetup{expansion=false,protrusion=false}'+'\n'+m[1]+'\n'+r'\par\endgroup',
                     converted,flags=re.M)
    return converted

licence=(out/'assets/GFDL-1.2.txt').read_text(encoding='utf8')
licence_appendix=r'''\appendix
\chapter*{GNU Free Documentation License, Version 1.2}
\addcontentsline{toc}{chapter}{GNU Free Documentation License, Version 1.2}
\begingroup\scriptsize
\begin{verbatim}
'''+licence+r'''
\end{verbatim}
\endgroup
'''
credit=r'''\author{GPT-6.1 Sol (OpenAI)\\Codex, Ultra setting}
\date{October 2026}
\begin{document}
\hypersetup{pageanchor=false}
\maketitle
\pagenumbering{roman}
\hypersetup{pageanchor=true}
\noindent Written and self-checked by the writing AI. No human or independent review is claimed.
Original contributions are dedicated under CC0 1.0. Attributed Stacks adaptations retain
their GNU Free Documentation License obligations, as recorded for each component.
The cumulative collection includes the complete version 1.2 licence below.
\par\medskip
\noindent Online course: \url{'''+base+r'''}.
\begingroup\small\tableofcontents\endgroup
\clearpage
\pagenumbering{arabic}
'''
catalog=json.loads((out/'catalogue.json').read_text(encoding='utf8'))
bodies=[]
for unit in catalog['courses'][0]['units']:
    uid=unit['id'];support='-S' in uid
    i=int(uid.rsplit('-',1)[1]) if not support else 0
    p=out/unit['source']; text=p.read_text(encoding='utf8'); body=convert(text)
    body=re.sub(r'\\label\{([^}]+)\}',lambda m:r'\label{'+uid+'-'+m[1]+'}',body)
    body=re.sub(r'\\hyperref\[([^]]+)\]',lambda m:r'\hyperref['+uid+'-'+m[1]+']',body)
    if support:
        body=re.sub(r'\\chapter\{([^}]+)\}',lambda m:r'\chapter*{'+m[1]+r'}\addcontentsline{toc}{chapter}{'+m[1]+'}',body,count=1)
    else:
        body=r'\setcounter{chapter}{'+str(i-1)+'}\n'+body
    bodies.append(body)
    front=credit
    gfdl=i in (3,5) or unit.get('license_expression','').startswith('GFDL')
    if not gfdl:
        front=front.replace('Attributed Stacks adaptations retain\ntheir GNU Free Documentation License obligations, as recorded for each component.\nThe cumulative collection includes the complete version 1.2 licence below.',
                            'Cited works retain their own licences.')
    title=text.splitlines()[0][2:]
    complete=preamble+r'\title{'+title+'}\n'+front+body+(licence_appendix if gfdl else '')+r'\end{document}'+'\n'
    (out/(uid+'.tex')).write_text(complete,encoding='utf8',newline='\n')

guide=[(out/'PREREQUISITES.md').read_text(encoding='utf8')]
guide_body=convert(''.join(guide)).replace(r'\chapter{Supporting prerequisites}',r'\chapter*{Supporting prerequisites}\addcontentsline{toc}{chapter}{Supporting prerequisites}')
complete=preamble+r'\title{Reductive group schemes}'+'\n'+credit+'\n'.join(bodies)+guide_body+licence_appendix+r'\end{document}'+'\n'
(out/'Reductive-group-schemes.tex').write_text(complete,encoding='utf8',newline='\n')
prerequisite=preamble+r'\title{Prerequisites for Reductive group schemes}'+'\n'+credit+convert((out/'PREREQUISITES.md').read_text(encoding='utf8'))+r'\end{document}'+'\n'
prerequisite=prerequisite.replace('Attributed Stacks adaptations retain\ntheir GNU Free Documentation License obligations, as recorded for each component.\nThe cumulative collection includes the complete version 1.2 licence below.','Cited works retain their own licences.')
(out/'Prerequisites.tex').write_text(prerequisite,encoding='utf8',newline='\n')
print('Created '+str(len(bodies)+2)+' complete TeX sources in the current supporting/main lesson order.')
