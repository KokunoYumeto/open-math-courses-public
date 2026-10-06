"""Draw the exact probability-code tree and support-condition example, CC0-1.0."""
from pathlib import Path
import argparse
import html
from PIL import Image, ImageDraw, ImageFont

COURSE=Path(__file__).resolve().parents[2]
FONT=COURSE/'finite-kernel-prerequisite/fonts/DejaVuSans.ttf'

def draw(output):
    output.mkdir(parents=True,exist_ok=True)
    width,height=1500,660
    image=Image.new('RGB',(width,height),'#ffffff')
    canvas=ImageDraw.Draw(image)
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">', '<rect width="1500" height="660" fill="white"/>', '<title>Consistent binary cylinder masses and the Borel support condition</title>', '<desc>Root mass1 splits into two masses1/2 and then four masses1/4. Fair Bernoulli probability gives the dense countable eventually-zero subset mass0, while codes of probabilities on that subset require mass1.</desc>']
    def line(x1,y1,x2,y2,color='#526783',stroke=3):
        canvas.line((x1,y1,x2,y2),fill=color,width=stroke)
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{stroke}"/>')
    def text(x,y,value,size=28,color='#1f2937',center=False):
        font=ImageFont.truetype(str(FONT),size)
        box=canvas.textbbox((0,0),value,font=font)
        left=x-(box[2]-box[0])/2 if center else x
        canvas.text((left,y),value,font=font,fill=color)
        anchor='middle' if center else 'start'
        svg.append(f'<text x="{x}" y="{y+size}" text-anchor="{anchor}" font-family="DejaVu Sans,sans-serif" font-size="{size}" fill="{color}">{html.escape(value)}</text>')
    def circle(x,y,r=32):
        canvas.ellipse((x-r,y-r,x+r,y+r),fill='#e5efff',outline='#345785',width=3)
        svg.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#e5efff" stroke="#345785" stroke-width="3"/>')
    text(52,25,'Borel probabilities: consistency and support',36)
    text(52,90,'K.P1: a parent equals its two children',26)
    line(742,92,742,570,color='#d8dde5',stroke=2)
    nodes=[(375,170,'C','1'),(210,305,'[0]','1/2'),(540,305,'[1]','1/2'),(115,445,'[00]','1/4'),(290,445,'[01]','1/4'),(460,445,'[10]','1/4'),(635,445,'[11]','1/4')]
    for parent,child in [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]:
        side=-25 if nodes[child][0]<nodes[parent][0] else 25
        line(nodes[parent][0]+side,nodes[parent][1]+24,nodes[child][0],nodes[child][1]-31)
    for x,y,label,mass in nodes:
        circle(x,y)
        text(x,y-18,mass,26,center=True)
        text(x,y+38,label,25,center=True)
    text(375,552,'1 = 1/2 + 1/2;   1/2 = 1/4 + 1/4',24,center=True)
    text(792,96,'K.P4: probabilities on a Borel subset X',26)
    text(812,165,'Code condition: mass(X) = 1',30,color='#345785')
    text(812,254,'X0 = eventually-zero sequences',27)
    text(812,310,'X0 is countable and Borel.',26)
    text(812,358,'Append zeros: X0 meets every cylinder.',24)
    text(812,420,'Fair Bernoulli mass(X0) = 0',28,color='#923131')
    text(812,486,'Finite-level consistency does not imply',24)
    text(812,520,'concentration on X0.',24)
    text(52,610,'Exact cylinder masses; existence, uniqueness and Borel evaluation: Theorem K.4A.',24)
    svg.append('</svg>')
    image.save(output/'probability-codes.png')
    (output/'probability-codes.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=COURSE/'finite-kernel-prerequisite/figures')
    draw(p.parse_args().output)
