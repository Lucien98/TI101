# AES S盒的代数正规型表示


为了搞清楚 [Re-Consolidating First-Order Masking Schemes](https://eprint.iacr.org/2020/890.pdf)<sup><a href="#ref1">[1]</a></sup>一文中对AES的S盒的分解，特撰此文。

我们首先分析$GF_2^4$ 上的求逆的代数正规型表达式，该表达式可从 [A More Efficient AES Threshold Implementation](https://link.springer.com/content/pdf/10.1007/978-3-319-06734-6_17.pdf)<sup><a href="#ref2">[2]</a></sup>附录中获取（其中$x_4$ 是lsb，大端序），具体公式如下所示。

\[
	\begin{align*}
	    &y_1 = x_3 + x_4 + x_1 x_3 + x_2 x_3 + x_2 x_3 x_4\\
		&y_2 = x_4 + x_1 x_3 + x_2 x_3 + x_2 x_4 + x_1 x_3 x_4\\
		&y_3 = x_1 + x_2 + x_1 x_3 + x_1 x_4 + x_1 x_2 x_4\\
		&y_4 = x_2 + x_1 x_3 + x_1 x_4 + x_2 x_4 + x_1 x_2 x_3\\
	\end{align*}
\]


如果用$a,b,c,d$ 表示输入(其中$a$ 为msb)，$x,y,z,t$ 表示输出（其中$x$ 为msb），则表达式为：

\[
	\begin{align*}
		&x = c + d + a c + b c + b c d\\
		&y = d + a c + b c + b d + a c d\\
		&z = a + b + a c + a d + a b d\\
		&t = b + a c + a d + b d + a b c\\    
	\end{align*}
\]

如果用$d,c,b,a$ 表示输入(其中$d$ 为msb)，$t,z,y,x$ 表示输出（其中$t$ 为msb），则表达式为：

\[
	\begin{align*}
		&t = c + a c + a d + b d + b c d\\
		&z = c + d + a d + b d + a c d\\
		&y = a + a c + b c + b d + a b d\\
		&x = a + b + b c + b d + a b c\\
	\end{align*}
\]

而文献[Re-Consolidating First-Order Masking Schemes](https://eprint.iacr.org/2020/890.pdf)<sup><a href="#ref1">[1]</a></sup>中的表达式为

\[
	\begin{align*}
		&x = a + b + d + b c + b d + c d + a b c\\
		&y = b + c + d + a c + b d + a b d + a c d\\
		&z = c + d + b c + c d + a c d + b c d\\
		&t = c + d + a d + b d + b c d\\
	\end{align*}
\]

无论如何，这两者都是不一致的。我曾给作者发了一封邮件问他是不是换了基，他的回复如下：

 	We didn't change the basis but we used an affine equivalent function of the GF(16) inverter
 	 in a way that the entire composition of AES S-box is correct. Of course, changing the function
 	  and basis would change the result of search. For some functions there is no solution 
 	  (like PRINCE S-box) while there are solutions for their affine equivalent functions.

这种对S盒分解的修改是无法通过简单的分析分析出来的，所以我们只能看源代码 [NullFresh](https://github.com/Chair-for-Security-Engineering/NullFresh)<sup><a href="#ref3">[3]</a></sup> 了。

根据源代码 [NullFresh](https://github.com/Chair-for-Security-Engineering/NullFresh)<sup><a href="#ref3">[3]</a></sup>，可以断定，在文献 <a href="#ref1">[1]</a> 中的表达式中，$a$ 是代表lsb，也就是说它是小端表示。

\[
	\begin{align*}
		&x = a + e + a e + b e + c e + a f + d f + a g + c g + b h + d h\\
		&y = d + h + a e + b e + d e + a f + c f + d f + b g + a h + b h\\
		&z = a + b + c + d + e + f + g + h + a e + b e + c e + d e + a f + c f + a g + b g + d g + a h + c h + d h\\
		&t = b + d + f + h + a e + c e + b f + d f + a g + c g + d g + b h + c h\\
	\end{align*}
\]



## 参考
1. <p name = "ref1">Re-Consolidating First-Order Masking Schemes.https://eprint.iacr.org/2020/890.pdf</p>
2. <p name = "ref2">A More Efficient AES Threshold Implementation.https://link.springer.com/content/pdf/10.1007/978-3-319-06734-6_17.pdf</p>
3. <p name = "ref3">NullFresh.https://github.com/Chair-for-Security-Engineering/NullFresh</p>


