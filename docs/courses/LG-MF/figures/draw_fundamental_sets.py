"""Reproduce the three fundamental-set diagrams from exact integer matrices."""
from pathlib import Path
from math import sin, cos, pi, sqrt
from PIL import Image, ImageDraw, ImageFont
out=Path(__file__).resolve().parent
out.mkdir(parents=True,exist_ok=True)
I=(1,0,0,1); S=(0,-1,1,0); T=(1,1,0,1)
def mul(a,b): return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
def power(a,n):
    r=I
    for _ in range(n): r=mul(r,a)
    return r
Y=25.
left=[-.5+1j*(sqrt(3)/2+(Y-sqrt(3)/2)*k/1200) for k in range(1201)]
right=[.5+1j*(sqrt(3)/2+(Y-sqrt(3)/2)*k/1200) for k in range(1201)]
arc=[complex(cos(2*pi/3-k*pi/3/1000),sin(2*pi/3-k*pi/3/1000)) for k in range(1001)]
boundary=list(reversed(left))+arc+right
panels=[('Gamma_0(2)',[I,S,mul(S,T)],(-1.15,.72),2.6),('Gamma_0(4)',[I,S]+[mul(S,power(T,k)) for k in range(1,4)]+[(1,0,2,1)],(-1.15,.78),1.65),('Gamma(2)',[I,T,S,mul(S,T),mul(T,S),mul(mul(S,T),S)],(-1.25,1.75),2.6)]
colors=['#dceaf6','#bed9ef','#93c6df','#65b1ca','#87c5b9','#cad9a4']
image=Image.new('RGB',(2400,1050),'white'); draw=ImageDraw.Draw(image)
font=ImageFont.load_default(size=26); titlefont=ImageFont.load_default(size=42)
draw.text((1200,40),'Fundamental sets assembled from the modular domain',font=titlefont,fill='#183b50',anchor='mt')
for panel,(title,mats,(xmin,xmax),ymax) in enumerate(panels):
    width,height=660,760; top=165; offset=panel*800+100
    tile=Image.new('RGB',(width,height),'white'); d=ImageDraw.Draw(tile)
    def xy(z): return ((z.real-xmin)/(xmax-xmin)*width,height-z.imag/ymax*height)
    for j,m in enumerate(mats):
        def transform(z): return (m[0]*z+m[1])/(m[2]*z+m[3])
        d.polygon([xy(transform(z)) for z in boundary],fill=colors[j])
        for side in (left,arc,right): d.line([xy(transform(z)) for z in side],fill='#355b72',width=2)
        x,y=xy(transform(1.3j))
        d.ellipse((x-18,y-18,x+18,y+18),fill='white')
        d.text((x,y),str(j+1),font=font,fill='#183b50',anchor='mm')
    image.paste(tile,(offset,top));draw.text((offset+width/2,112),title,font=titlefont,fill='#183b50',anchor='mt')
    draw.line((offset,top+height,offset+width,top+height),fill='#355b72',width=2)
    draw.line((offset,top,offset,top+height),fill='#355b72',width=2)
    for value in range(int(xmin)-1,int(xmax)+2):
        if xmin<=value<=xmax:
            x=offset+(value-xmin)/(xmax-xmin)*width;draw.line((x,top+height,x,top+height+8),fill='#355b72',width=2);draw.text((x,top+height+16),str(value),font=font,fill='#355b72',anchor='mt')
    for value in (0,1,2):
        if value<ymax:
            y=top+height-value/ymax*height;draw.text((offset-15,y),str(value),font=font,fill='#355b72',anchor='rm')
    draw.text((offset+width/2,1000),'Re z',font=font,fill='#355b72',anchor='mm')
    draw.text((offset-40,top-25),'Im z',font=font,fill='#355b72',anchor='mm')
image.save(out/'congruence-fundamental-sets.png')
print('saved original sampled-geodesic diagram')
