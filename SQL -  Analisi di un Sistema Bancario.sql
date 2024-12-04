/*
Progetto  Analisi di un Sistema Bancario
Studente : Stefano Conforto

Ogni indicatore va riferito al singolo id_cliente.

Età
Numero di transazioni in uscita su tutti i conti
Numero di transazioni in entrata su tutti i conti
Importo transato in uscita su tutti i conti
Importo transato in entrata su tutti i conti
Numero totale di conti posseduti
Numero di conti posseduti per tipologia (un indicatore per tipo)
Numero di transazioni in uscita per tipologia (un indicatore per tipo)
Numero di transazioni in entrata per tipologia (un indicatore per tipo)
Importo transato in uscita per tipologia di conto (un indicatore per tipo)
Importo transato in entrata per tipologia di conto (un indicatore per tipo)
*/


select 
subquery.id_cliente,
subquery.eta, /*Età*/
sum(subquery.tran_uscita) as tu, /* numero transazioni in uscita su tutti i conti*/
sum(subquery.tran_entrata) as te,/* numero transazioni in entrata su tutti i conti*/ 
sum(subquery.€_uscita) as €_usc,/*Importo transato in uscita su tutti i conti*/ 
sum(subquery.€_entrata) as €_ent,/*Importo transato in entrata su tutti i conti*/ 
sum(subquery.conteggio_conti) as n_conti, /*Numero totale di conti posseduti*/
/*Numero di conti posseduti per tipologia (un indicatore per tipo)*/
sum(case when subquery.conto_tipo_0 = 1 then 1 else 0 end) as n_cont_base,
sum(case when subquery.conto_tipo_1 = 1 then 1 else 0 end) as n_cont_businness,
sum(case when subquery.conto_tipo_2 = 1 then 1 else 0 end) as n_cont_privati,
sum(case when subquery.conto_tipo_3 = 1 then 1 else 0 end) as n_cont_famiglie,
/*Numero di transazioni in uscita per tipologia (un indicatore per tipo)*/
sum(subquery.usc_num_trans_3) as num_trans_3_usc,
sum(subquery.usc_num_trans_4) as num_trans_4_usc,
sum(subquery.usc_num_trans_5) as num_trans_5_usc,
sum(subquery.usc_num_trans_6) as num_trans_6_usc,
sum(subquery.usc_num_trans_7) as num_trans_7_usc,
/*Numero di transazioni in entrata per tipologia (un indicatore per tipo)*/
sum(subquery.ent_num_trans_0) as num_trans_0_ent,
sum(subquery.ent_num_trans_1) as num_trans_1_ent,
sum(subquery.ent_num_trans_2) as num_trans_2_ent,
/*Importo transato in entrata per tipologia di conto (un indicatore per tipo)*/
sum(subquery.€_ent_conto_base) as conto_base_€_ent,
sum(subquery.€_ent_conto_businnes) as conto_businnes_€_ent,
sum(subquery.€_ent_conto_privati) as conto_privati_€_ent,
sum(subquery.€_ent_conto_famiglie) as conto_famiglie_€_ent,
/*Importo transato in uscita per tipologia di conto (un indicatore per tipo)*/
sum(€_usc_conto_base) as conto_base_€_usc,
sum(€_usc_conto_businnes) as conto_businnes_€_usc,
sum(€_usc_conto_privati) as conto_privati_€_usc,
sum(€_usc_conto_famiglie) as conto_famiglie_€_usc

from

(select
c.id_cliente,
year(current_date())-left(cli.data_nascita,4) as eta,
c.id_conto,
/* numero transazioni in uscita su tutti i conti*/
sum(case when t.id_tipo_trans in(3,4,5,6,7) then 1 else 0 end) as tran_uscita,
/* numero transazioni in entrata su tutti i conti*/ 
sum(case when t.id_tipo_trans in (0,1,2) then 1 else 0 end) as tran_entrata, 
/*Importo transato in uscita su tutti i conti*/    
sum(case when t.id_tipo_trans in (3,4,5,6,7) then t.importo else 0 end) as €_uscita,
/*Importo transato in entrata su tutti i conti*/ 
sum(case when t.id_tipo_trans in (0,1,2) then t.importo else 0 end) as €_entrata,
/*Numero totale di conti posseduti*/
count(distinct c.id_conto) as conteggio_conti, 
/*Numero di conti posseduti per tipologia (un indicatore per tipo)*/
max(  case when c.id_tipo_conto = 0 then 1 else 0 end) as conto_tipo_0, 
max(  case when c.id_tipo_conto = 1 then 1 else 0 end) as conto_tipo_1,
max(  case when c.id_tipo_conto = 2 then 1 else 0 end) as conto_tipo_2,
max(  case when c.id_tipo_conto = 3 then 1 else 0 end) as conto_tipo_3,

/*Numero di transazioni in uscita per tipologia (un indicatore per tipo)*/
sum(case when t.id_tipo_trans=3 then 1 else 0 end) as usc_num_trans_3,
sum(case when t.id_tipo_trans=4 then 1 else 0 end) as usc_num_trans_4,
sum(case when t.id_tipo_trans=5 then 1 else 0 end) as usc_num_trans_5,
sum(case when t.id_tipo_trans=6 then 1 else 0 end) as usc_num_trans_6,
sum(case when t.id_tipo_trans=7 then 1 else 0 end) as usc_num_trans_7,
/*Numero di transazioni in entrata per tipologia (un indicatore per tipo)*/
sum(case when t.id_tipo_trans=0 then 1 else 0 end) as ent_num_trans_0, 
sum(case when t.id_tipo_trans=1 then 1 else 0 end) as ent_num_trans_1,
sum(case when t.id_tipo_trans=2 then 1 else 0 end) as ent_num_trans_2,
/*Importo transato in entrata per tipologia di conto (un indicatore per tipo)*/

sum(case when (t.id_tipo_trans in(0,1,2) and c.id_tipo_conto=0) then t.importo else 0 end) as €_ent_conto_base,
sum(case when (t.id_tipo_trans in(0,1,2) and c.id_tipo_conto=1) then t.importo else 0 end) as €_ent_conto_businnes,
sum(case when (t.id_tipo_trans in(0,1,2) and c.id_tipo_conto=2) then t.importo else 0 end) as €_ent_conto_privati,
sum(case when (t.id_tipo_trans in(0,1,2) and c.id_tipo_conto=3) then t.importo else 0 end) as €_ent_conto_famiglie,

/*Importo transato in uscita per tipologia di conto (un indicatore per tipo)*/
sum(case when (t.id_tipo_trans in(3,4,5,6,7) and c.id_tipo_conto=0) then t.importo else 0 end) as €_usc_conto_base,
sum(case when (t.id_tipo_trans in(3,4,5,6,7) and c.id_tipo_conto=1) then t.importo else 0 end) as €_usc_conto_businnes,
sum(case when (t.id_tipo_trans in(3,4,5,6,7) and c.id_tipo_conto=2) then t.importo else 0 end) as €_usc_conto_privati,
sum(case when (t.id_tipo_trans in(3,4,5,6,7) and c.id_tipo_conto=3) then t.importo else 0 end) as €_usc_conto_famiglie


from
transazioni as t
right join conto as c
on t.id_conto=c.id_conto
left join cliente as cli
on c.id_cliente=cli.id_cliente
group by 1,2,3
order by 1
) as subquery
left join conto as cn
on subquery.id_conto=cn.id_conto
group by 1,2;

