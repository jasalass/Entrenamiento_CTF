# SOLUCIONES (SPOILERS)

La web valida por hash; esto es solo para comprobar.

```
D01 [Crypto    N1] Cesar / desplazamiento fijo                           ->  FLAG{d01_crypto_qlff}
D01 [Encoding  N1] Capas de codificacion (1): B64                        ->  FLAG{d01_encoding_61jl}
D01 [Stego     N1] LSB en RGB                                            ->  FLAG{d01_stego_cn66}
D01 [Forensics N1] Payload Base64 en log                                 ->  FLAG{d01_forensics_jlua}
D01 [OSINT     N1] Correlacion (2 fuentes)                               ->  FLAG{d01_osint_8066}
D01 [Reversing N1] Deshacer transformacion N1                            ->  FLAG{d01_reversing_ila6}
D01 [Web       N1] Web: inyeccion de comandos                            ->  FLAG{d01_web_hsq9}
D01 [Pwn       N1] Privesc: binario SUID                                 ->  FLAG{d01_pwn_69pp}
D02 [Crypto    N1] Cesar con numeros de por medio                        ->  FLAG{d02_crypto_cwdp}
D02 [Encoding  N1] Capas de codificacion (1): HEX                        ->  FLAG{d02_encoding_02af}
D02 [Stego     N1] Metadatos ocultos                                     ->  FLAG{d02_stego_c5k8}
D02 [Forensics N1] Hex plano a binario                                   ->  FLAG{d02_forensics_1cpy}
D02 [OSINT     N1] Correlacion (2 fuentes)                               ->  FLAG{d02_osint_yvbk}
D02 [Reversing N1] Deshacer transformacion N1                            ->  FLAG{d02_reversing_b9n8}
D02 [Web       N2] Web: manipulacion de cookie                           ->  FLAG{d02_web_ugrs}
D02 [Pwn       N2] Privesc: sudo find (GTFOBins)                         ->  FLAG{d02_pwn_8phc}
D03 [Crypto    N1] Cesar en mayusculas                                   ->  FLAG{d03_crypto_9pyi}
D03 [Encoding  N1] Capas de codificacion (1): B32                        ->  FLAG{d03_encoding_damc}
D03 [Stego     N1] Datos tras el EOF                                     ->  FLAG{d03_stego_5zch}
D03 [Forensics N1] Carving de un ZIP                                     ->  FLAG{d03_forensics_jesm}
D03 [OSINT     N1] Correlacion (2 fuentes)                               ->  FLAG{d03_osint_8qi9}
D03 [Reversing N1] Deshacer transformacion N1                            ->  FLAG{d03_reversing_qg5m}
D03 [Web       N2] Web: IDOR                                             ->  FLAG{d03_web_gjqv}
D03 [Pwn       N2] Privesc: sudo awk (GTFOBins)                          ->  FLAG{d03_pwn_00eh}
D04 [Crypto    N1] Cesar sin espacios                                    ->  FLAG{d04_crypto_ynav}
D04 [Encoding  N1] Capas de codificacion (1): BIN                        ->  FLAG{d04_encoding_vcvq}
D04 [Stego     N1] Caracteres invisibles                                 ->  FLAG{d04_stego_sbpb}
D04 [Forensics N1] Stream gzip embebido                                  ->  FLAG{d04_forensics_u0as}
D04 [OSINT     N1] Correlacion (2 fuentes)                               ->  FLAG{d04_osint_i7j2}
D04 [Reversing N1] Deshacer transformacion N1                            ->  FLAG{d04_reversing_h7f4}
D04 [Web       N2] Web: path traversal (LFI)                             ->  FLAG{d04_web_zq1d}
D04 [Pwn       N3] Privesc: /etc/passwd escribible                       ->  FLAG{d04_pwn_f2md}
D05 [Crypto    N1] Cesar con la clave en el enunciado                    ->  FLAG{d05_crypto_d69d}
D05 [Encoding  N1] Capas de codificacion (1): B85                        ->  FLAG{d05_encoding_0hxx}
D05 [Stego     N1] LSB canal azul                                        ->  FLAG{d05_stego_stb3}
D05 [Forensics N1] Busca en el ruido                                     ->  FLAG{d05_forensics_g130}
D05 [OSINT     N1] Correlacion (2 fuentes)                               ->  FLAG{d05_osint_l4gn}
D05 [Reversing N1] Deshacer transformacion N1                            ->  FLAG{d05_reversing_prsm}
D05 [Web       N3] Web: SSRF                                             ->  FLAG{d05_web_l89k}
D05 [Pwn       N3] Privesc: PATH hijack de SUID                          ->  FLAG{d05_pwn_vu5n}
D06 [Crypto    N1] Cesar envuelto en Base64                              ->  FLAG{d06_crypto_oh76}
D06 [Encoding  N1] Capas de codificacion (1): ROT13                      ->  FLAG{d06_encoding_3kt1}
D06 [Stego     N1] LSB en RGB                                            ->  FLAG{d06_stego_x6gu}
D06 [Forensics N1] Payload Base64 en log                                 ->  FLAG{d06_forensics_o6dy}
D06 [OSINT     N1] Correlacion (2 fuentes)                               ->  FLAG{d06_osint_psr7}
D06 [Reversing N1] Deshacer transformacion N1                            ->  FLAG{d06_reversing_rudc}
D06 [Web       N3] Web: SQL injection (login)                            ->  FLAG{d06_web_mlcs}
D06 [Pwn       N3] Privesc: cron con script writable                     ->  FLAG{d06_pwn_eld2}
D07 [Crypto    N1] Cesar progresivo (clave que avanza)                   ->  FLAG{d07_crypto_tew3}
D07 [Encoding  N1] Capas de codificacion (1): REV                        ->  FLAG{d07_encoding_25zt}
D07 [Stego     N1] Metadatos ocultos                                     ->  FLAG{d07_stego_bo8e}
D07 [Forensics N1] Hex plano a binario                                   ->  FLAG{d07_forensics_wbk2}
D07 [OSINT     N1] Correlacion (2 fuentes)                               ->  FLAG{d07_osint_st0x}
D07 [Reversing N1] Deshacer transformacion N1                            ->  FLAG{d07_reversing_7ju8}
D07 [Web       N3] Web: SQLi UNION                                       ->  FLAG{d07_web_ssfe}
D07 [Pwn       N3] Privesc: sudo python3                                 ->  FLAG{d07_pwn_8rho}
D08 [Crypto    N2] Vigenere con clave conocida                           ->  FLAG{d08_crypto_b7v8}
D08 [Encoding  N2] Capas de codificacion (2): B64+ROT13                  ->  FLAG{d08_encoding_dbj4}
D08 [Stego     N2] Datos tras el EOF                                     ->  FLAG{d08_stego_b787}
D08 [Forensics N2] Carving de un ZIP                                     ->  FLAG{d08_forensics_pblh}
D08 [OSINT     N2] Correlacion (3 fuentes)                               ->  FLAG{d08_osint_cd3ucg}
D08 [Reversing N2] Deshacer transformacion N2                            ->  FLAG{d08_reversing_z45n}
D08 [Web       N4] Web: JWT alg:none                                     ->  FLAG{d08_web_3xmh}
D08 [Pwn       N4] Privesc: capability cap_dac_read_search               ->  FLAG{d08_pwn_jchg}
D09 [Crypto    N2] Vigenere: solo sabes el largo de la clave             ->  FLAG{d09_crypto_j23i}
D09 [Encoding  N2] Capas de codificacion (2): B64+REV                    ->  FLAG{d09_encoding_y15f}
D09 [Stego     N2] Caracteres invisibles                                 ->  FLAG{d09_stego_k93f}
D09 [Forensics N2] Stream gzip embebido                                  ->  FLAG{d09_forensics_ulqr}
D09 [OSINT     N2] Correlacion (3 fuentes)                               ->  FLAG{d09_osint_l3c0s3}
D09 [Reversing N2] Deshacer transformacion N2                            ->  FLAG{d09_reversing_kzwp}
D09 [Web       N4] Web: SSTI (Jinja2)                                    ->  FLAG{d09_web_mi6z}
D09 [Pwn       N4] Privesc: capability cap_setuid                        ->  FLAG{d09_pwn_qg28}
D10 [Crypto    N2] Vigenere: clave por analisis de frecuencia            ->  FLAG{d10_crypto_76r4}
D10 [Encoding  N2] Capas de codificacion (2): B64+HEX                    ->  FLAG{d10_encoding_aqsg}
D10 [Stego     N2] LSB canal azul                                        ->  FLAG{d10_stego_pm11}
D10 [Forensics N2] Busca en el ruido                                     ->  FLAG{d10_forensics_6rlu}
D10 [OSINT     N2] Correlacion (3 fuentes)                               ->  FLAG{d10_osint_s1jaeb}
D10 [Reversing N2] Deshacer transformacion N2                            ->  FLAG{d10_reversing_wa4s}
D10 [Web       N4] Web: XXE                                              ->  FLAG{d10_web_5i2e}
D10 [Pwn       N4] Privesc: sudo + LD_PRELOAD                            ->  FLAG{d10_pwn_8mpk}
D11 [Crypto    N2] Vigenere: encuentra el largo de clave (Kasiski)       ->  FLAG{d11_crypto_8o05}
D11 [Encoding  N2] Capas de codificacion (2): B32+B64                    ->  FLAG{d11_encoding_uwn3}
D11 [Stego     N2] LSB en RGB                                            ->  FLAG{d11_stego_ede5}
D11 [Forensics N2] Payload Base64 en log                                 ->  FLAG{d11_forensics_huec}
D11 [OSINT     N2] Correlacion (3 fuentes)                               ->  FLAG{d11_osint_sjkq1k}
D11 [Reversing N2] Deshacer transformacion N2                            ->  FLAG{d11_reversing_turj}
D11 [Web       N1] Web: inyeccion de comandos                            ->  FLAG{d11_web_hdzr}
D11 [Pwn       N1] Privesc: binario SUID                                 ->  FLAG{d11_pwn_tlod}
D12 [Crypto    N2] Vigenere: Kasiski de nuevo, texto distinto            ->  FLAG{d12_crypto_fufd}
D12 [Encoding  N2] Capas de codificacion (2): HEX+ROT13                  ->  FLAG{d12_encoding_7751}
D12 [Stego     N2] Metadatos ocultos                                     ->  FLAG{d12_stego_enp5}
D12 [Forensics N2] Hex plano a binario                                   ->  FLAG{d12_forensics_4r7u}
D12 [OSINT     N2] Correlacion (3 fuentes)                               ->  FLAG{d12_osint_4u205z}
D12 [Reversing N2] Deshacer transformacion N2                            ->  FLAG{d12_reversing_87vh}
D12 [Web       N2] Web: manipulacion de cookie                           ->  FLAG{d12_web_63sh}
D12 [Pwn       N2] Privesc: sudo find (GTFOBins)                         ->  FLAG{d12_pwn_8tr6}
D13 [Crypto    N2] Vigenere: clave larga, mas columnas                   ->  FLAG{d13_crypto_yo0s}
D13 [Encoding  N2] Capas de codificacion (2): B32+REV                    ->  FLAG{d13_encoding_0wbe}
D13 [Stego     N2] Datos tras el EOF                                     ->  FLAG{d13_stego_dmtt}
D13 [Forensics N2] Carving de un ZIP                                     ->  FLAG{d13_forensics_nlni}
D13 [OSINT     N2] Correlacion (3 fuentes)                               ->  FLAG{d13_osint_4eypzt}
D13 [Reversing N2] Deshacer transformacion N2                            ->  FLAG{d13_reversing_27mn}
D13 [Web       N2] Web: IDOR                                             ->  FLAG{d13_web_5pwr}
D13 [Pwn       N2] Privesc: sudo awk (GTFOBins)                          ->  FLAG{d13_pwn_v0jp}
D14 [Crypto    N2] Vigenere: ataque completo sin ninguna pista           ->  FLAG{d14_crypto_y4gd}
D14 [Encoding  N2] Capas de codificacion (2): BIN+B32                    ->  FLAG{d14_encoding_kq34}
D14 [Stego     N2] Caracteres invisibles                                 ->  FLAG{d14_stego_hg53}
D14 [Forensics N2] Stream gzip embebido                                  ->  FLAG{d14_forensics_td55}
D14 [OSINT     N2] Correlacion (3 fuentes)                               ->  FLAG{d14_osint_nvbhc3}
D14 [Reversing N2] Deshacer transformacion N2                            ->  FLAG{d14_reversing_0uss}
D14 [Web       N2] Web: path traversal (LFI)                             ->  FLAG{d14_web_dbwu}
D14 [Pwn       N3] Privesc: /etc/passwd escribible                       ->  FLAG{d14_pwn_3tzs}
D15 [Crypto    N2] Vigenere: capstone del nivel                          ->  FLAG{d15_crypto_xfaa}
D15 [Encoding  N2] Capas de codificacion (2): B85+ROT13                  ->  FLAG{d15_encoding_3ndj}
D15 [Stego     N2] LSB canal rojo                                        ->  FLAG{d15_stego_bt8i}
D15 [Forensics N2] Busca en el ruido                                     ->  FLAG{d15_forensics_snwo}
D15 [OSINT     N2] Correlacion (3 fuentes)                               ->  FLAG{d15_osint_3f04eo}
D15 [Reversing N2] Deshacer transformacion N2                            ->  FLAG{d15_reversing_luq3}
D15 [Web       N3] Web: SSRF                                             ->  FLAG{d15_web_fdos}
D15 [Pwn       N3] Privesc: PATH hijack de SUID                          ->  FLAG{d15_pwn_9uob}
D16 [Crypto    N3] XOR de un byte, con el flag al inicio                 ->  FLAG{d16_crypto_nw8m}
D16 [Encoding  N3] Capas de codificacion (3): B64+REV+ROT13              ->  FLAG{d16_encoding_i6xk}
D16 [Stego     N3] LSB en RGB                                            ->  FLAG{d16_stego_jnqe}
D16 [Forensics N3] Payload Base64 en log                                 ->  FLAG{d16_forensics_hvdf}
D16 [OSINT     N3] Correlacion (4 fuentes)                               ->  FLAG{d16_osint_b9gyjg5u}
D16 [Reversing N3] Deshacer transformacion N3                            ->  FLAG{d16_reversing_r73u}
D16 [Web       N3] Web: SQL injection (login)                            ->  FLAG{d16_web_7ck0}
D16 [Pwn       N3] Privesc: cron con script writable                     ->  FLAG{d16_pwn_8qwb}
D17 [Crypto    N3] XOR de un byte, a ciegas                              ->  FLAG{d17_crypto_ewku}
D17 [Encoding  N3] Capas de codificacion (3): B64+ROT13+HEX              ->  FLAG{d17_encoding_995g}
D17 [Stego     N3] Metadatos ocultos                                     ->  FLAG{d17_stego_hkqw}
D17 [Forensics N3] Hex plano a binario                                   ->  FLAG{d17_forensics_fuzs}
D17 [OSINT     N3] Correlacion (4 fuentes)                               ->  FLAG{d17_osint_648k5su0}
D17 [Reversing N3] Deshacer transformacion N3                            ->  FLAG{d17_reversing_5fgk}
D17 [Web       N3] Web: SQLi UNION                                       ->  FLAG{d17_web_qlpa}
D17 [Pwn       N3] Privesc: sudo python3                                 ->  FLAG{d17_pwn_dlc9}
D18 [Crypto    N3] XOR de clave repetida, clave conocida                 ->  FLAG{d18_crypto_q1cx}
D18 [Encoding  N3] Capas de codificacion (3): B32+HEX+REV                ->  FLAG{d18_encoding_91oe}
D18 [Stego     N3] Datos tras el EOF                                     ->  FLAG{d18_stego_hog1}
D18 [Forensics N3] Carving de un ZIP                                     ->  FLAG{d18_forensics_uty9}
D18 [OSINT     N3] Correlacion (4 fuentes)                               ->  FLAG{d18_osint_yh5q48f6}
D18 [Reversing N3] Deshacer transformacion N3                            ->  FLAG{d18_reversing_o73x}
D18 [Web       N4] Web: JWT alg:none                                     ->  FLAG{d18_web_xa8j}
D18 [Pwn       N4] Privesc: capability cap_dac_read_search               ->  FLAG{d18_pwn_twij}
D19 [Crypto    N3] XOR de clave repetida: solo sabes el largo            ->  FLAG{d19_crypto_3s87}
D19 [Encoding  N3] Capas de codificacion (3): B64+ROT13+B32              ->  FLAG{d19_encoding_157y}
D19 [Stego     N3] Caracteres invisibles                                 ->  FLAG{d19_stego_5aak}
D19 [Forensics N3] Stream gzip embebido                                  ->  FLAG{d19_forensics_wffy}
D19 [OSINT     N3] Correlacion (4 fuentes)                               ->  FLAG{d19_osint_82ftgspt}
D19 [Reversing N3] Deshacer transformacion N3                            ->  FLAG{d19_reversing_vfux}
D19 [Web       N4] Web: SSTI (Jinja2)                                    ->  FLAG{d19_web_3dvh}
D19 [Pwn       N4] Privesc: capability cap_setuid                        ->  FLAG{d19_pwn_5iae}
D20 [Crypto    N3] XOR clave repetida: encuentra el largo (Hamming)      ->  FLAG{d20_crypto_hpg6}
D20 [Encoding  N3] Capas de codificacion (3): B85+HEX+ROT13              ->  FLAG{d20_encoding_jnpf}
D20 [Stego     N3] LSB canal azul                                        ->  FLAG{d20_stego_l0fy}
D20 [Forensics N3] Busca en el ruido                                     ->  FLAG{d20_forensics_o97o}
D20 [OSINT     N3] Correlacion (4 fuentes)                               ->  FLAG{d20_osint_3ie1lyvh}
D20 [Reversing N3] Deshacer transformacion N3                            ->  FLAG{d20_reversing_5486}
D20 [Web       N4] Web: XXE                                              ->  FLAG{d20_web_dzua}
D20 [Pwn       N4] Privesc: sudo + LD_PRELOAD                            ->  FLAG{d20_pwn_986l}
D21 [Crypto    N3] XOR clave repetida: Hamming de nuevo                  ->  FLAG{d21_crypto_tq7a}
D21 [Encoding  N3] Capas de codificacion (3): BIN+REV+HEX                ->  FLAG{d21_encoding_q590}
D21 [Stego     N3] LSB en RGB                                            ->  FLAG{d21_stego_r4u9}
D21 [Forensics N3] Payload Base64 en log                                 ->  FLAG{d21_forensics_s1ah}
D21 [OSINT     N3] Correlacion (4 fuentes)                               ->  FLAG{d21_osint_rni0aowh}
D21 [Reversing N3] Deshacer transformacion N3                            ->  FLAG{d21_reversing_whoa}
D21 [Web       N1] Web: inyeccion de comandos                            ->  FLAG{d21_web_gv5h}
D21 [Pwn       N1] Privesc: binario SUID                                 ->  FLAG{d21_pwn_snzk}
D22 [Crypto    N3] XOR clave repetida: Hamming + frecuencia por columna  ->  FLAG{d22_crypto_k3cv}
D22 [Encoding  N3] Capas de codificacion (3): HEX+ROT13+B64              ->  FLAG{d22_encoding_fn0w}
D22 [Stego     N3] Metadatos ocultos                                     ->  FLAG{d22_stego_dvil}
D22 [Forensics N3] Hex plano a binario                                   ->  FLAG{d22_forensics_wmbf}
D22 [OSINT     N3] Correlacion (4 fuentes)                               ->  FLAG{d22_osint_auj1ss1y}
D22 [Reversing N3] Deshacer transformacion N3                            ->  FLAG{d22_reversing_l3b3}
D22 [Web       N2] Web: manipulacion de cookie                           ->  FLAG{d22_web_u5vv}
D22 [Pwn       N2] Privesc: sudo find (GTFOBins)                         ->  FLAG{d22_pwn_c212}
D23 [Crypto    N3] XOR clave repetida: ataque completo (capstone)        ->  FLAG{d23_crypto_j7sb}
D23 [Encoding  N3] Capas de codificacion (3): HEX+B32+REV                ->  FLAG{d23_encoding_1a1m}
D23 [Stego     N3] Datos tras el EOF                                     ->  FLAG{d23_stego_r6ez}
D23 [Forensics N3] Carving de un ZIP                                     ->  FLAG{d23_forensics_ctxi}
D23 [OSINT     N3] Correlacion (4 fuentes)                               ->  FLAG{d23_osint_ljj94236}
D23 [Reversing N3] Deshacer transformacion N3                            ->  FLAG{d23_reversing_zart}
D23 [Web       N2] Web: IDOR                                             ->  FLAG{d23_web_bxkg}
D23 [Pwn       N2] Privesc: sudo awk (GTFOBins)                          ->  FLAG{d23_pwn_uy1e}
D24 [Crypto    N4] RSA factorizable (n chico)                            ->  FLAG{d24_crypto_7c4h}
D24 [Encoding  N4] Capas de codificacion (4): B64+HEX+REV+ROT13          ->  FLAG{d24_encoding_2i3d}
D24 [Stego     N4] Caracteres invisibles                                 ->  FLAG{d24_stego_frvf}
D24 [Forensics N4] Stream gzip embebido                                  ->  FLAG{d24_forensics_w06o}
D24 [OSINT     N4] Correlacion (5 fuentes + senuelo)                     ->  FLAG{d24_osint_ataigwe718}
D24 [Reversing N4] Deshacer transformacion N4                            ->  FLAG{d24_reversing_6fu8}
D24 [Web       N2] Web: path traversal (LFI)                             ->  FLAG{d24_web_5d8y}
D24 [Pwn       N3] Privesc: /etc/passwd escribible                       ->  FLAG{d24_pwn_h86i}
D25 [Crypto    N4] Crackear hash MD5 (mascara)                           ->  FLAG{d25_crypto_ezmm}
D25 [Encoding  N4] Capas de codificacion (4): B32+REV+ROT13+HEX          ->  FLAG{d25_encoding_03qe}
D25 [Stego     N4] LSB canal rojo                                        ->  FLAG{d25_stego_6j79}
D25 [Forensics N4] Busca en el ruido                                     ->  FLAG{d25_forensics_pqlo}
D25 [OSINT     N4] Correlacion (5 fuentes + senuelo)                     ->  FLAG{d25_osint_lc06sz3ppt}
D25 [Reversing N4] Deshacer transformacion N4                            ->  FLAG{d25_reversing_75zl}
D25 [Web       N3] Web: SSRF                                             ->  FLAG{d25_web_8ec7}
D25 [Pwn       N3] Privesc: PATH hijack de SUID                          ->  FLAG{d25_pwn_wkls}
D26 [Crypto    N4] RSA con p y q muy cercanos (Fermat)                   ->  FLAG{d26_crypto_l8fz}
D26 [Encoding  N4] Capas de codificacion (4): HEX+ROT13+B64+REV          ->  FLAG{d26_encoding_9drd}
D26 [Stego     N4] LSB en RGB                                            ->  FLAG{d26_stego_ba4q}
D26 [Forensics N4] Payload Base64 en log                                 ->  FLAG{d26_forensics_r8km}
D26 [OSINT     N4] Correlacion (5 fuentes + senuelo)                     ->  FLAG{d26_osint_m0csgx4qc6}
D26 [Reversing N4] Deshacer transformacion N4                            ->  FLAG{d26_reversing_wcgg}
D26 [Web       N3] Web: SQL injection (login)                            ->  FLAG{d26_web_cdj2}
D26 [Pwn       N3] Privesc: cron con script writable                     ->  FLAG{d26_pwn_d8fw}
D27 [Crypto    N4] Crackear hash MD5 (diccionario)                       ->  FLAG{d27_crypto_erjrm}
D27 [Encoding  N4] Capas de codificacion (4): B64+ROT13+HEX+B85          ->  FLAG{d27_encoding_tj6v}
D27 [Stego     N4] Metadatos ocultos                                     ->  FLAG{d27_stego_u1b3}
D27 [Forensics N4] Hex plano a binario                                   ->  FLAG{d27_forensics_jsyg}
D27 [OSINT     N4] Correlacion (5 fuentes + senuelo)                     ->  FLAG{d27_osint_8pygdbe2s6}
D27 [Reversing N4] Deshacer transformacion N4                            ->  FLAG{d27_reversing_izpa}
D27 [Web       N3] Web: SQLi UNION                                       ->  FLAG{d27_web_uahw}
D27 [Pwn       N3] Privesc: sudo python3                                 ->  FLAG{d27_pwn_07jy}
D28 [Crypto    N4] RSA: exponente chico sin relleno (raiz cubica)        ->  FLAG{d28_crypto_qrao}
D28 [Encoding  N4] Capas de codificacion (4): HEX+REV+B32+ROT13          ->  FLAG{d28_encoding_95ye}
D28 [Stego     N4] Datos tras el EOF                                     ->  FLAG{d28_stego_k9kx}
D28 [Forensics N4] Carving de un ZIP                                     ->  FLAG{d28_forensics_g70l}
D28 [OSINT     N4] Correlacion (5 fuentes + senuelo)                     ->  FLAG{d28_osint_2damo6wolu}
D28 [Reversing N4] Deshacer transformacion N4                            ->  FLAG{d28_reversing_p9dk}
D28 [Web       N4] Web: JWT alg:none                                     ->  FLAG{d28_web_94af}
D28 [Pwn       N4] Privesc: capability cap_dac_read_search               ->  FLAG{d28_pwn_z3w5}
D29 [Crypto    N4] Identifica el hash antes de crackearlo                ->  FLAG{d29_crypto_oMgc}
D29 [Encoding  N4] Capas de codificacion (4): B32+REV+B64+HEX            ->  FLAG{d29_encoding_529p}
D29 [Stego     N4] Caracteres invisibles                                 ->  FLAG{d29_stego_96j3}
D29 [Forensics N4] Stream gzip embebido                                  ->  FLAG{d29_forensics_xeuk}
D29 [OSINT     N4] Correlacion (5 fuentes + senuelo)                     ->  FLAG{d29_osint_0ohux0hv6a}
D29 [Reversing N4] Deshacer transformacion N4                            ->  FLAG{d29_reversing_ilm3}
D29 [Web       N4] Web: SSTI (Jinja2)                                    ->  FLAG{d29_web_vxyn}
D29 [Pwn       N4] Privesc: capability cap_setuid                        ->  FLAG{d29_pwn_9iko}
D30 [Crypto    N4] RSA capstone: Fermat con primos grandes               ->  FLAG{d30_crypto_28rz12}
D30 [Encoding  N4] Capas de codificacion (4): B85+HEX+ROT13+REV          ->  FLAG{d30_encoding_morv}
D30 [Stego     N4] LSB canal rojo                                        ->  FLAG{d30_stego_r5r3}
D30 [Forensics N4] Busca en el ruido                                     ->  FLAG{d30_forensics_37w2}
D30 [OSINT     N4] Correlacion (5 fuentes + senuelo)                     ->  FLAG{d30_osint_u9mqdbpdt5}
D30 [Reversing N4] Deshacer transformacion N4                            ->  FLAG{d30_reversing_hagf}
D30 [Web       N4] Web: XXE                                              ->  FLAG{d30_web_1neh}
D30 [Pwn       N4] Privesc: sudo + LD_PRELOAD                            ->  FLAG{d30_pwn_chn3}
D31 [Pwn-Bin   N1] Pwn-Bin: overflow de variable local      ->  FLAG{d31_pwnbin_overflow_y6y7}
D32 [Pwn-Bin   N1] Pwn-Bin: overflow de variable local      ->  FLAG{d32_pwnbin_overflow_o7b4}
D33 [Pwn-Bin   N1] Pwn-Bin: overflow de variable local      ->  FLAG{d33_pwnbin_overflow_89os}
D34 [Pwn-Bin   N2] Pwn-Bin: ret2win (secuestro de flujo)    ->  FLAG{d34_pwnbin_ret2win_uysa}
D35 [Pwn-Bin   N2] Pwn-Bin: ret2win (secuestro de flujo)    ->  FLAG{d35_pwnbin_ret2win_xy5d}
D36 [Pwn-Bin   N2] Pwn-Bin: ret2win (secuestro de flujo)    ->  FLAG{d36_pwnbin_ret2win_114z}
D37 [Pwn-Bin   N3] Pwn-Bin: format string - fuga (leak)     ->  FLAG{d37_pwnbin_fmtleak_7tr3}
D38 [Pwn-Bin   N3] Pwn-Bin: format string - fuga (leak)     ->  FLAG{d38_pwnbin_fmtleak_h99p}
D39 [Pwn-Bin   N3] Pwn-Bin: format string - fuga (leak)     ->  FLAG{d39_pwnbin_fmtleak_vz2s}
D40 [Pwn-Bin   N4] Pwn-Bin: format string - escritura (%n)  ->  FLAG{d40_pwnbin_fmtwrite_bw58}
D41 [Pwn-Bin   N4] Pwn-Bin: format string - escritura (%n)  ->  FLAG{d41_pwnbin_fmtwrite_h7c5}
D42 [Pwn-Bin   N4] Pwn-Bin: format string - escritura (%n)  ->  FLAG{d42_pwnbin_fmtwrite_o7ry}
D43 [Reversing N1] Reversing (binario ciego): XOR constante ->  FLAG{d43_revbin_xorc_6tql}
D44 [Reversing N1] Reversing (binario ciego): XOR constante ->  FLAG{d44_revbin_xorc_awu7}
D45 [Reversing N2] Reversing (binario ciego): XOR posicional ->  FLAG{d45_revbin_xorpos_fuul}
D46 [Reversing N2] Reversing (binario ciego): XOR posicional ->  FLAG{d46_revbin_xorpos_azje}
D47 [Reversing N3] Reversing (binario ciego): suma + XOR    ->  FLAG{d47_revbin_addxor_e9wa}
D48 [Reversing N3] Reversing (binario ciego): suma + XOR    ->  FLAG{d48_revbin_addxor_csfb}
D49 [Reversing N4] Reversing (binario ciego): retroalimentacion ->  FLAG{d49_revbin_feedback_6hp1}
D50 [Reversing N4] Reversing (binario ciego): retroalimentacion ->  FLAG{d50_revbin_feedback_460j}
```
