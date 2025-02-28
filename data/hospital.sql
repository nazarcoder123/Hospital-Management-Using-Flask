PGDMP  %    4                 }            hospital    17.2    17.2 J    ~           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    16579    hospital    DATABASE     {   CREATE DATABASE hospital WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_India.1252';
    DROP DATABASE hospital;
                     postgres    false            �            1259    16611    appointment    TABLE     �   CREATE TABLE public.appointment (
    app_id integer NOT NULL,
    pat_id integer NOT NULL,
    doc_id integer NOT NULL,
    appointment_date date NOT NULL
);
    DROP TABLE public.appointment;
       public         heap r       postgres    false            �            1259    16610    appointment_app_id_seq    SEQUENCE     �   CREATE SEQUENCE public.appointment_app_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.appointment_app_id_seq;
       public               postgres    false    224            �           0    0    appointment_app_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.appointment_app_id_seq OWNED BY public.appointment.app_id;
          public               postgres    false    223            �            1259    16644 
   department    TABLE     }   CREATE TABLE public.department (
    department_id integer NOT NULL,
    name text NOT NULL,
    head_id integer NOT NULL
);
    DROP TABLE public.department;
       public         heap r       postgres    false            �            1259    16643    department_department_id_seq    SEQUENCE     �   CREATE SEQUENCE public.department_department_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.department_department_id_seq;
       public               postgres    false    229            �           0    0    department_department_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.department_department_id_seq OWNED BY public.department.department_id;
          public               postgres    false    228            �            1259    16591    doctor    TABLE     �   CREATE TABLE public.doctor (
    doc_id integer NOT NULL,
    doc_first_name text NOT NULL,
    doc_last_name text NOT NULL,
    doc_ph_no text NOT NULL,
    doc_date date DEFAULT CURRENT_DATE,
    doc_address text NOT NULL
);
    DROP TABLE public.doctor;
       public         heap r       postgres    false            �            1259    16590    doctor_doc_id_seq    SEQUENCE     �   CREATE SEQUENCE public.doctor_doc_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.doctor_doc_id_seq;
       public               postgres    false    220            �           0    0    doctor_doc_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.doctor_doc_id_seq OWNED BY public.doctor.doc_id;
          public               postgres    false    219            �            1259    16635 
   medication    TABLE     �   CREATE TABLE public.medication (
    code integer NOT NULL,
    name text NOT NULL,
    brand text NOT NULL,
    description text
);
    DROP TABLE public.medication;
       public         heap r       postgres    false            �            1259    16634    medication_code_seq    SEQUENCE     �   CREATE SEQUENCE public.medication_code_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.medication_code_seq;
       public               postgres    false    227            �           0    0    medication_code_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.medication_code_seq OWNED BY public.medication.code;
          public               postgres    false    226            �            1259    16601    nurse    TABLE     �   CREATE TABLE public.nurse (
    nur_id integer NOT NULL,
    nur_first_name text NOT NULL,
    nur_last_name text NOT NULL,
    nur_ph_no text NOT NULL,
    nur_date date DEFAULT CURRENT_DATE,
    nur_address text NOT NULL
);
    DROP TABLE public.nurse;
       public         heap r       postgres    false            �            1259    16600    nurse_nur_id_seq    SEQUENCE     �   CREATE SEQUENCE public.nurse_nur_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.nurse_nur_id_seq;
       public               postgres    false    222            �           0    0    nurse_nur_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.nurse_nur_id_seq OWNED BY public.nurse.nur_id;
          public               postgres    false    221            �            1259    16581    patient    TABLE       CREATE TABLE public.patient (
    pat_id integer NOT NULL,
    pat_first_name text NOT NULL,
    pat_last_name text NOT NULL,
    pat_insurance_no text NOT NULL,
    pat_ph_no text NOT NULL,
    pat_date date DEFAULT CURRENT_DATE,
    pat_address text NOT NULL
);
    DROP TABLE public.patient;
       public         heap r       postgres    false            �            1259    16580    patient_pat_id_seq    SEQUENCE     �   CREATE SEQUENCE public.patient_pat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.patient_pat_id_seq;
       public               postgres    false    218            �           0    0    patient_pat_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.patient_pat_id_seq OWNED BY public.patient.pat_id;
          public               postgres    false    217            �            1259    16696 
   prescribes    TABLE     �   CREATE TABLE public.prescribes (
    doc_id integer NOT NULL,
    pat_id integer NOT NULL,
    med_code integer NOT NULL,
    p_date date NOT NULL,
    app_id integer NOT NULL,
    dose integer NOT NULL
);
    DROP TABLE public.prescribes;
       public         heap r       postgres    false            �            1259    16658 	   procedure    TABLE     p   CREATE TABLE public.procedure (
    code integer NOT NULL,
    name text NOT NULL,
    cost integer NOT NULL
);
    DROP TABLE public.procedure;
       public         heap r       postgres    false            �            1259    16657    procedure_code_seq    SEQUENCE     �   CREATE SEQUENCE public.procedure_code_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.procedure_code_seq;
       public               postgres    false    231            �           0    0    procedure_code_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.procedure_code_seq OWNED BY public.procedure.code;
          public               postgres    false    230            �            1259    16627    room    TABLE     x   CREATE TABLE public.room (
    room_no integer NOT NULL,
    room_type text NOT NULL,
    available integer NOT NULL
);
    DROP TABLE public.room;
       public         heap r       postgres    false            �            1259    16666 	   undergoes    TABLE     �   CREATE TABLE public.undergoes (
    pat_id integer NOT NULL,
    proc_code integer NOT NULL,
    u_date date NOT NULL,
    doc_id integer,
    nur_id integer,
    room_no integer
);
    DROP TABLE public.undergoes;
       public         heap r       postgres    false            �           2604    16614    appointment app_id    DEFAULT     x   ALTER TABLE ONLY public.appointment ALTER COLUMN app_id SET DEFAULT nextval('public.appointment_app_id_seq'::regclass);
 A   ALTER TABLE public.appointment ALTER COLUMN app_id DROP DEFAULT;
       public               postgres    false    224    223    224            �           2604    16647    department department_id    DEFAULT     �   ALTER TABLE ONLY public.department ALTER COLUMN department_id SET DEFAULT nextval('public.department_department_id_seq'::regclass);
 G   ALTER TABLE public.department ALTER COLUMN department_id DROP DEFAULT;
       public               postgres    false    228    229    229            �           2604    16594    doctor doc_id    DEFAULT     n   ALTER TABLE ONLY public.doctor ALTER COLUMN doc_id SET DEFAULT nextval('public.doctor_doc_id_seq'::regclass);
 <   ALTER TABLE public.doctor ALTER COLUMN doc_id DROP DEFAULT;
       public               postgres    false    219    220    220            �           2604    16638    medication code    DEFAULT     r   ALTER TABLE ONLY public.medication ALTER COLUMN code SET DEFAULT nextval('public.medication_code_seq'::regclass);
 >   ALTER TABLE public.medication ALTER COLUMN code DROP DEFAULT;
       public               postgres    false    227    226    227            �           2604    16604    nurse nur_id    DEFAULT     l   ALTER TABLE ONLY public.nurse ALTER COLUMN nur_id SET DEFAULT nextval('public.nurse_nur_id_seq'::regclass);
 ;   ALTER TABLE public.nurse ALTER COLUMN nur_id DROP DEFAULT;
       public               postgres    false    222    221    222            �           2604    16584    patient pat_id    DEFAULT     p   ALTER TABLE ONLY public.patient ALTER COLUMN pat_id SET DEFAULT nextval('public.patient_pat_id_seq'::regclass);
 =   ALTER TABLE public.patient ALTER COLUMN pat_id DROP DEFAULT;
       public               postgres    false    217    218    218            �           2604    16661    procedure code    DEFAULT     p   ALTER TABLE ONLY public.procedure ALTER COLUMN code SET DEFAULT nextval('public.procedure_code_seq'::regclass);
 =   ALTER TABLE public.procedure ALTER COLUMN code DROP DEFAULT;
       public               postgres    false    231    230    231            r          0    16611    appointment 
   TABLE DATA           O   COPY public.appointment (app_id, pat_id, doc_id, appointment_date) FROM stdin;
    public               postgres    false    224   YX       w          0    16644 
   department 
   TABLE DATA           B   COPY public.department (department_id, name, head_id) FROM stdin;
    public               postgres    false    229   �X       n          0    16591    doctor 
   TABLE DATA           i   COPY public.doctor (doc_id, doc_first_name, doc_last_name, doc_ph_no, doc_date, doc_address) FROM stdin;
    public               postgres    false    220   �X       u          0    16635 
   medication 
   TABLE DATA           D   COPY public.medication (code, name, brand, description) FROM stdin;
    public               postgres    false    227   MY       p          0    16601    nurse 
   TABLE DATA           h   COPY public.nurse (nur_id, nur_first_name, nur_last_name, nur_ph_no, nur_date, nur_address) FROM stdin;
    public               postgres    false    222   �Y       l          0    16581    patient 
   TABLE DATA           |   COPY public.patient (pat_id, pat_first_name, pat_last_name, pat_insurance_no, pat_ph_no, pat_date, pat_address) FROM stdin;
    public               postgres    false    218   .Z       {          0    16696 
   prescribes 
   TABLE DATA           T   COPY public.prescribes (doc_id, pat_id, med_code, p_date, app_id, dose) FROM stdin;
    public               postgres    false    233   �Z       y          0    16658 	   procedure 
   TABLE DATA           5   COPY public.procedure (code, name, cost) FROM stdin;
    public               postgres    false    231   �Z       s          0    16627    room 
   TABLE DATA           =   COPY public.room (room_no, room_type, available) FROM stdin;
    public               postgres    false    225   [       z          0    16666 	   undergoes 
   TABLE DATA           W   COPY public.undergoes (pat_id, proc_code, u_date, doc_id, nur_id, room_no) FROM stdin;
    public               postgres    false    232   Y[       �           0    0    appointment_app_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.appointment_app_id_seq', 8, true);
          public               postgres    false    223            �           0    0    department_department_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.department_department_id_seq', 1, false);
          public               postgres    false    228            �           0    0    doctor_doc_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.doctor_doc_id_seq', 3, true);
          public               postgres    false    219            �           0    0    medication_code_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.medication_code_seq', 1, false);
          public               postgres    false    226            �           0    0    nurse_nur_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.nurse_nur_id_seq', 2, true);
          public               postgres    false    221            �           0    0    patient_pat_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.patient_pat_id_seq', 3, true);
          public               postgres    false    217            �           0    0    procedure_code_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.procedure_code_seq', 1, false);
          public               postgres    false    230            �           2606    16616    appointment appointment_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_pkey PRIMARY KEY (app_id);
 F   ALTER TABLE ONLY public.appointment DROP CONSTRAINT appointment_pkey;
       public                 postgres    false    224            �           2606    16651    department department_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (department_id);
 D   ALTER TABLE ONLY public.department DROP CONSTRAINT department_pkey;
       public                 postgres    false    229            �           2606    16599    doctor doctor_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.doctor
    ADD CONSTRAINT doctor_pkey PRIMARY KEY (doc_id);
 <   ALTER TABLE ONLY public.doctor DROP CONSTRAINT doctor_pkey;
       public                 postgres    false    220            �           2606    16642    medication medication_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.medication
    ADD CONSTRAINT medication_pkey PRIMARY KEY (code);
 D   ALTER TABLE ONLY public.medication DROP CONSTRAINT medication_pkey;
       public                 postgres    false    227            �           2606    16609    nurse nurse_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.nurse
    ADD CONSTRAINT nurse_pkey PRIMARY KEY (nur_id);
 :   ALTER TABLE ONLY public.nurse DROP CONSTRAINT nurse_pkey;
       public                 postgres    false    222            �           2606    16589    patient patient_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.patient
    ADD CONSTRAINT patient_pkey PRIMARY KEY (pat_id);
 >   ALTER TABLE ONLY public.patient DROP CONSTRAINT patient_pkey;
       public                 postgres    false    218            �           2606    16700    prescribes prescribes_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.prescribes
    ADD CONSTRAINT prescribes_pkey PRIMARY KEY (doc_id, pat_id, med_code, p_date);
 D   ALTER TABLE ONLY public.prescribes DROP CONSTRAINT prescribes_pkey;
       public                 postgres    false    233    233    233    233            �           2606    16665    procedure procedure_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.procedure
    ADD CONSTRAINT procedure_pkey PRIMARY KEY (code);
 B   ALTER TABLE ONLY public.procedure DROP CONSTRAINT procedure_pkey;
       public                 postgres    false    231            �           2606    16633    room room_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.room
    ADD CONSTRAINT room_pkey PRIMARY KEY (room_no);
 8   ALTER TABLE ONLY public.room DROP CONSTRAINT room_pkey;
       public                 postgres    false    225            �           2606    16670    undergoes undergoes_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.undergoes
    ADD CONSTRAINT undergoes_pkey PRIMARY KEY (pat_id, proc_code, u_date);
 B   ALTER TABLE ONLY public.undergoes DROP CONSTRAINT undergoes_pkey;
       public                 postgres    false    232    232    232            �           2606    16622 #   appointment appointment_doc_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_doc_id_fkey FOREIGN KEY (doc_id) REFERENCES public.doctor(doc_id);
 M   ALTER TABLE ONLY public.appointment DROP CONSTRAINT appointment_doc_id_fkey;
       public               postgres    false    224    220    4797            �           2606    16617 #   appointment appointment_pat_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_pat_id_fkey FOREIGN KEY (pat_id) REFERENCES public.patient(pat_id);
 M   ALTER TABLE ONLY public.appointment DROP CONSTRAINT appointment_pat_id_fkey;
       public               postgres    false    224    218    4795            �           2606    16652 "   department department_head_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_head_id_fkey FOREIGN KEY (head_id) REFERENCES public.doctor(doc_id);
 L   ALTER TABLE ONLY public.department DROP CONSTRAINT department_head_id_fkey;
       public               postgres    false    229    4797    220            �           2606    16716 !   prescribes prescribes_app_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.prescribes
    ADD CONSTRAINT prescribes_app_id_fkey FOREIGN KEY (app_id) REFERENCES public.appointment(app_id);
 K   ALTER TABLE ONLY public.prescribes DROP CONSTRAINT prescribes_app_id_fkey;
       public               postgres    false    4801    233    224            �           2606    16701 !   prescribes prescribes_doc_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.prescribes
    ADD CONSTRAINT prescribes_doc_id_fkey FOREIGN KEY (doc_id) REFERENCES public.doctor(doc_id);
 K   ALTER TABLE ONLY public.prescribes DROP CONSTRAINT prescribes_doc_id_fkey;
       public               postgres    false    220    233    4797            �           2606    16711 #   prescribes prescribes_med_code_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.prescribes
    ADD CONSTRAINT prescribes_med_code_fkey FOREIGN KEY (med_code) REFERENCES public.medication(code);
 M   ALTER TABLE ONLY public.prescribes DROP CONSTRAINT prescribes_med_code_fkey;
       public               postgres    false    227    4805    233            �           2606    16706 !   prescribes prescribes_pat_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.prescribes
    ADD CONSTRAINT prescribes_pat_id_fkey FOREIGN KEY (pat_id) REFERENCES public.patient(pat_id);
 K   ALTER TABLE ONLY public.prescribes DROP CONSTRAINT prescribes_pat_id_fkey;
       public               postgres    false    4795    233    218            �           2606    16681    undergoes undergoes_doc_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.undergoes
    ADD CONSTRAINT undergoes_doc_id_fkey FOREIGN KEY (doc_id) REFERENCES public.doctor(doc_id);
 I   ALTER TABLE ONLY public.undergoes DROP CONSTRAINT undergoes_doc_id_fkey;
       public               postgres    false    220    232    4797            �           2606    16686    undergoes undergoes_nur_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.undergoes
    ADD CONSTRAINT undergoes_nur_id_fkey FOREIGN KEY (nur_id) REFERENCES public.nurse(nur_id);
 I   ALTER TABLE ONLY public.undergoes DROP CONSTRAINT undergoes_nur_id_fkey;
       public               postgres    false    4799    222    232            �           2606    16671    undergoes undergoes_pat_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.undergoes
    ADD CONSTRAINT undergoes_pat_id_fkey FOREIGN KEY (pat_id) REFERENCES public.patient(pat_id);
 I   ALTER TABLE ONLY public.undergoes DROP CONSTRAINT undergoes_pat_id_fkey;
       public               postgres    false    4795    232    218            �           2606    16676 "   undergoes undergoes_proc_code_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.undergoes
    ADD CONSTRAINT undergoes_proc_code_fkey FOREIGN KEY (proc_code) REFERENCES public.procedure(code);
 L   ALTER TABLE ONLY public.undergoes DROP CONSTRAINT undergoes_proc_code_fkey;
       public               postgres    false    232    231    4809            �           2606    16691     undergoes undergoes_room_no_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.undergoes
    ADD CONSTRAINT undergoes_room_no_fkey FOREIGN KEY (room_no) REFERENCES public.room(room_no);
 J   ALTER TABLE ONLY public.undergoes DROP CONSTRAINT undergoes_room_no_fkey;
       public               postgres    false    4803    232    225            r   @   x�U���0C�s�.E�C�ð�����Kvd8,�!%Y0?����iV/���n`���s /��6      w      x�3��K--���O��4����� ;g      n   i   x�3�t)RpK̬���H��47��0�4423�4202�50"N�ʔԢĤ�.#�r�������΂��Ĕ�DNC#cS3sKd]��ŉ�y
�E)�y\1z\\\ \�O      u   U   x��1�  ��}E77|�����Th���{�b6 �[�SL��'�w�4S���0��0����v*Z��^���(c�"���c      p   l   x�M�K�  �ur
.@'���]�������ۥ3o�4�
-i��Lԉc"`����>&���5�s1��u��E�E��:�mS�q�v�I��$��k�)��p~ ��q q      l   b   x�M�K�0E���^�C��ŅMU�u��	�JWwt��V�{1�u��9"H?ĔGeK|�����]&��f'��64��}���7_�g6zvDtԐU      {   !   x�3�4�44�4202�50�5� ��b���� >\%      y   ;   x�344��H�,R()J�+.�I�+�45 .CC#��ļ�T�\jbIn*P�� ,���� �      s   -   x�340�tI�)��4�240�.-H-҅�E�!"��\1z\\\ $-�      z   6   x�Uɱ  �:�d���A�(@/}sIa:�8Õ(��t�1~����i=     