INSERT INTO departments (name, location, responsible_id) VALUES 
-- CENÁRIO 1: OBRAS (Responsáveis: Lucas Gerente, Alice Analista, Marta Analista)
('d9cd69c2-7690-4d3f-baae-ea8e96e323aa', 'Canteiro de Obras - Projeto Alfa', 'Rodovia BR-101, Km 50 - Central de Campo', '39f68707-fa3e-4a4b-a2d7-6a8405d765d4'),
('e8841c8d-5641-4349-a3b6-6a5d53fb475a', 'Canteiro de Obras - Projeto Beta', 'Centro da Cidade - Escritório Provisório', '27799e0a-3055-4f35-af51-5643fc97fb08'),
('5537e1f0-9480-405b-87fb-dba79ec6ffa1', 'Escritório de Engenharia da Obra', 'Sede da Obra Alfa - Sala de Reuniões 1', 'f001110b-8173-482e-8161-546d7354b299'),

-- CENÁRIO 2: GESTÃO E SUPORTE (Responsáveis: Analistas Maria e Pedro, Gerente João)
('9bdbcb3c-1aad-4179-994c-29ab4a50f58f', 'Suporte Técnico de Campo (TI)', 'Escritório Central - 1º Andar, Sala 101', 'f001110b-8173-482e-8161-546d7354b299'),
('5adfd3e0-50bc-4b37-a216-799a818feedb', 'Logística e Almoxarifado de TI', 'Centro de Distribuição - Prédio L, Setor 5', '99a6a6f3-f35a-4a54-872f-95e789e989aa'),
('5dea7663-05bb-43b2-9f75-ac92fe4140dd', 'Gerência de Ativos (Patrimônio)', 'Escritório Central - 4º Andar, Sala 402', '0457a162-8504-42a7-a64a-f3707e769294'),

-- CENÁRIO 3: ÁREAS ADMINISTRATIVAS/AUXILIARES (Com e Sem Responsável)
('8249748d-8320-4e99-84a0-cba81a38615a', 'Departamento Comercial', 'Escritório Central - 5º Andar, Ala Sul', NULL), -- Sem responsável
('da3791af-165e-4766-bf95-2e047dd85074', 'Recursos Humanos (RH)', 'Escritório Central - 2º Andar, Sala de Treinamento', 'cf28555e-0bbe-4f98-a51c-77801492f0aa'),
('b6e07ea4-527c-4731-bdbf-bd501b2a1807', 'Financeiro e Controladoria', 'Escritório Central - 3º Andar, Data Seguro', NULL), -- Sem responsável

-- CENÁRIO 4: ÁREA DE TESTES E REPARO (Responsável: Pedro Analista)
('24616230-a688-491b-8e99-2fe51d2d324e', 'Laboratório de Configuração e Reparo', 'Subsolo - Sala B-05 (Acesso Restrito)', '99a6a6f3-f35a-4a54-872f-95e789e989aa');