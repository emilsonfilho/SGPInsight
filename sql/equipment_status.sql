INSERT INTO equipment_status (name) VALUES 
('ad10386e-4409-4f85-ab66-86fc68e43967', 'Operacional em Campo'),         -- 1. Equipamento em uso ativo (ex: tablet robusto em canteiro)
('7928f418-b6ec-4678-a8a1-62523e746509', 'Operacional em Escritório'),    -- 2. Equipamento em uso ativo (ex: desktop/laptop na matriz)
('4f7e4913-d84c-4c4e-8590-ab042f2ffa62', 'Em Manutenção (Laboratório)'),  -- 3. Em reparo no laboratório interno (Cenário 4 do departments)
('69dc98bb-cad1-41b8-a34a-d741b01a6475', 'Em Manutenção (Terceirizada)'), -- 4. Equipamento enviado para reparo externo
('106bff4e-37e0-4100-a3ea-3ae3a655f76f', 'Aguardando Configuração'),      -- 5. Novo equipamento ou recondicionado, aguardando instalação de software
('c1df3c71-6cf7-45c0-98fa-b6ae87d2f53f', 'Aguardando Descarte'),          -- 6. Equipamento obsoleto ou quebrado, aguardando aprovação final
('3fde1877-6862-4e93-a513-6720b4531d21', 'Descartado/Baixado'),           -- 7. Equipamento removido do inventário
('4a6dbd66-944e-46c4-9288-7b6338196814', 'Em Estoque (Pronto)'),          -- 8. Equipamento em estoque, pronto para ser alocado a um usuário/localização
('b0de06e6-065d-4d00-83d5-0a88654d0a7a', 'Em Estoque (Reserva)');         -- 9. Equipamento em estoque, designado como reserva imediata para falhas críticas