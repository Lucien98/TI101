## AES
### AES Sbox
    { 8'h63, 8'h7c, 8'h77, 8'h7b, 8'hf2, 8'h6b, 8'h6f, 8'hc5, 8'h30, 8'h01, 8'h67, 8'h2b, 8'hfe, 8'hd7, 8'hab, 8'h76,
      8'hca, 8'h82, 8'hc9, 8'h7d, 8'hfa, 8'h59, 8'h47, 8'hf0, 8'had, 8'hd4, 8'ha2, 8'haf, 8'h9c, 8'ha4, 8'h72, 8'hc0,
      8'hb7, 8'hfd, 8'h93, 8'h26, 8'h36, 8'h3f, 8'hf7, 8'hcc, 8'h34, 8'ha5, 8'he5, 8'hf1, 8'h71, 8'hd8, 8'h31, 8'h15,
      8'h04, 8'hc7, 8'h23, 8'hc3, 8'h18, 8'h96, 8'h05, 8'h9a, 8'h07, 8'h12, 8'h80, 8'he2, 8'heb, 8'h27, 8'hb2, 8'h75,
      8'h09, 8'h83, 8'h2c, 8'h1a, 8'h1b, 8'h6e, 8'h5a, 8'ha0, 8'h52, 8'h3b, 8'hd6, 8'hb3, 8'h29, 8'he3, 8'h2f, 8'h84,
      8'h53, 8'hd1, 8'h00, 8'hed, 8'h20, 8'hfc, 8'hb1, 8'h5b, 8'h6a, 8'hcb, 8'hbe, 8'h39, 8'h4a, 8'h4c, 8'h58, 8'hcf,
      8'hd0, 8'hef, 8'haa, 8'hfb, 8'h43, 8'h4d, 8'h33, 8'h85, 8'h45, 8'hf9, 8'h02, 8'h7f, 8'h50, 8'h3c, 8'h9f, 8'ha8,
      8'h51, 8'ha3, 8'h40, 8'h8f, 8'h92, 8'h9d, 8'h38, 8'hf5, 8'hbc, 8'hb6, 8'hda, 8'h21, 8'h10, 8'hff, 8'hf3, 8'hd2,
      8'hcd, 8'h0c, 8'h13, 8'hec, 8'h5f, 8'h97, 8'h44, 8'h17, 8'hc4, 8'ha7, 8'h7e, 8'h3d, 8'h64, 8'h5d, 8'h19, 8'h73,
      8'h60, 8'h81, 8'h4f, 8'hdc, 8'h22, 8'h2a, 8'h90, 8'h88, 8'h46, 8'hee, 8'hb8, 8'h14, 8'hde, 8'h5e, 8'h0b, 8'hdb,
      8'he0, 8'h32, 8'h3a, 8'h0a, 8'h49, 8'h06, 8'h24, 8'h5c, 8'hc2, 8'hd3, 8'hac, 8'h62, 8'h91, 8'h95, 8'he4, 8'h79,
      8'he7, 8'hc8, 8'h37, 8'h6d, 8'h8d, 8'hd5, 8'h4e, 8'ha9, 8'h6c, 8'h56, 8'hf4, 8'hea, 8'h65, 8'h7a, 8'hae, 8'h08,
      8'hba, 8'h78, 8'h25, 8'h2e, 8'h1c, 8'ha6, 8'hb4, 8'hc6, 8'he8, 8'hdd, 8'h74, 8'h1f, 8'h4b, 8'hbd, 8'h8b, 8'h8a,
      8'h70, 8'h3e, 8'hb5, 8'h66, 8'h48, 8'h03, 8'hf6, 8'h0e, 8'h61, 8'h35, 8'h57, 8'hb9, 8'h86, 8'hc1, 8'h1d, 8'h9e,
      8'he1, 8'hf8, 8'h98, 8'h11, 8'h69, 8'hd9, 8'h8e, 8'h94, 8'h9b, 8'h1e, 8'h87, 8'he9, 8'hce, 8'h55, 8'h28, 8'hdf,
      8'h8c, 8'ha1, 8'h89, 8'h0d, 8'hbf, 8'he6, 8'h42, 8'h68, 8'h41, 8'h99, 8'h2d, 8'h0f, 8'hb0, 8'h54, 8'hbb, 8'h16
    };

### GF256 inversion

       0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
 	0  0  1 8d f6 cb 52 7b d1 e8 4f 29 c0 b0 e1 e5 c7
 	1 74 b4 aa 4b 99 2b 60 5f 58 3f fd cc ff 40 ee b2
 	2 3a 6e 5a f1 55 4d a8 c9 c1  a 98 15 30 44 a2 c2
 	3 2c 45 92 6c f3 39 66 42 f2 35 20 6f 77 bb 59 19
 	4 1d fe 37 67 2d 31 f5 69 a7 64 ab 13 54 25 e9  9
 	5 ed 5c  5 ca 4c 24 87 bf 18 3e 22 f0 51 ec 61 17
 	6 16 5e af d3 49 a6 36 43 f4 47 91 df 33 93 21 3b
 	7 79 b7 97 85 10 b5 ba 3c b6 70 d0  6 a1 fa 81 82
 	8 83 7e 7f 80 96 73 be 56 9b 9e 95 d9 f7  2 b9 a4
 	9 de 6a 32 6d d8 8a 84 72 2a 14 9f 88 f9 dc 89 9a
 	a fb 7c 2e c3 8f b8 65 48 26 c8 12 4a ce e7 d2 62
 	b  c e0 1f ef 11 75 78 71 a5 8e 76 3d bd bc 86 57
 	c  b 28 2f a3 da d4 e4  f a9 27 53  4 1b fc ac e6
 	d 7a  7 ae 63 c5 db e2 ea 94 8b c4 d5 9d f8 90 6b
 	e b1  d d6 eb c6  e cf ad  8 4e d7 e3 5d 50 1e b3
 	f 5b 23 38 34 68 46  3 8c dd 9c 7d a0 cd 1a 41 1c
