Add-Type -AssemblyName System.Drawing
$bmp=[Drawing.Bitmap]::new(1460,1120)
$g=[Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode=[Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.Clear([Drawing.Color]::White)
$font=[Drawing.Font]::new('Segoe UI',22)
$small=[Drawing.Font]::new('Segoe UI',16)
$title=[Drawing.Font]::new('Segoe UI',26,[Drawing.FontStyle]::Bold)
$ink=[Drawing.SolidBrush]::new([Drawing.Color]::FromArgb(22,38,58))
$blue=[Drawing.Pen]::new([Drawing.Color]::FromArgb(32,88,155),3)
$orange=[Drawing.Pen]::new([Drawing.Color]::FromArgb(179,85,10),3)
$cap=[Drawing.Drawing2D.AdjustableArrowCap]::new(5,6)
$blue.CustomEndCap=$cap
$orange.CustomEndCap=$cap
$sf=[Drawing.StringFormat]::new()
$sf.Alignment=[Drawing.StringAlignment]::Center
$sf.LineAlignment=[Drawing.StringAlignment]::Center
$nl=[char]10
function Box($x,$y,$label) {
 $rect=[Drawing.RectangleF]::new($x,$y,380,116)
 $g.FillRectangle([Drawing.SolidBrush]::new([Drawing.Color]::FromArgb(239,246,253)),$rect)
 $g.DrawRectangle([Drawing.Pen]::new([Drawing.Color]::FromArgb(100,130,160),2),$x,$y,380,116)
 $g.DrawString($label,$font,$ink,$rect,$sf)
}
function Label($x,$y,$w,$h,$label) {
 $rect=[Drawing.RectangleF]::new($x,$y,$w,$h)
 $g.FillRectangle([Drawing.Brushes]::White,$rect)
 $g.DrawString($label,$small,$ink,$rect,$sf)
}
$g.DrawString('Supported integrability and the carrier sector',$title,$ink,[Drawing.RectangleF]::new(20,10,1420,60),$sf)
Box 40 140 ('Integrable support'+$nl+'action of ψ')
Box 540 140 ('Integrable support'+$nl+'action of ψ̇')
Box 1040 140 ('c ⊗ 1 ≲ c ⊗ ρ'+$nl+'≲ 1 ⊗ ρ ∼ 1 ⊗ 1')
Box 40 465 'ψ ≲ Φ'
Box 540 465 'ψ̇ ≲ Φ'
Box 1040 465 'p(ψ̇) ≤ d'
Box 540 790 ('Continuous carrier'+$nl+'projection orbit')
$g.DrawLine($blue,425,180,530,180)
$g.DrawLine($blue,535,220,430,220)
Label 414 90 134 65 ('CI27'+$nl+'tensor / cut')
$g.DrawLine($blue,925,198,1030,198)
Label 911 86 130 87 ('CI28–37'+$nl+'full-support'+$nl+'intertwiner')
$g.DrawLine($blue,1215,266,810,455)
Label 940 315 340 72 ('CI38, CI21–23'+$nl+'balanced row cancellation')
$g.DrawLine($blue,535,502,430,502)
$g.DrawLine($blue,425,546,530,546)
Label 415 590 130 68 ('CI24'+$nl+'amplify / cut')
$g.DrawLine($blue,925,502,1030,502)
$g.DrawLine($blue,1035,546,930,546)
Label 915 590 132 66 ('CI10'+$nl+'carrier order')
$g.DrawLine($blue,225,455,225,266)
Label 63 320 325 68 ('CI25–27'+$nl+'dual average and fixed cut')
$g.DrawLine($blue,1170,591,860,780)
$g.DrawLine($orange,935,864,1350,590)
Label 850 650 280 70 ('CI4: center-flow'+$nl+'identification J')
Label 1050 750 350 80 ('CI17–18: rational join'+$nl+'DS: dominant uniqueness')
$g.DrawString('Every action is on its actual weight support. Zero weights are included.',$small,$ink,[Drawing.RectangleF]::new(35,936,1390,35),$sf)
$g.DrawString('Orange arrow: pointwise dominant uniqueness on the original central support.',$small,$ink,[Drawing.RectangleF]::new(35,974,1390,35),$sf)
$g.DrawString('Proofs: CI10, CI17–18, CI21–27, CI28–39; OA-FLOW-DS Sections 2–6.',$small,$ink,[Drawing.RectangleF]::new(35,1020,1390,35),$sf)
$g.DrawString('Context: M. Takesaki, Theory of Operator Algebras II, XII.4, pp. 403–405, 417–419.',$small,$ink,[Drawing.RectangleF]::new(35,1062,1390,35),$sf)
$ms=[IO.MemoryStream]::new()
$bmp.Save($ms,[Drawing.Imaging.ImageFormat]::Png)
[IO.File]::WriteAllBytes((Join-Path $PSScriptRoot 'cgf-mechanism.png'),$ms.ToArray())
$g.Dispose()
$bmp.Dispose()
$ms.Dispose()
