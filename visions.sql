CREATE OR REPLACE VIEW vw_maintenance_details AS
SELECT 
    m.id, 
    m.description, 
    m.created_at, 
    m.finished_at,

    CASE
        WHEN m.finished_at IS NULL THEN 'active'
        ELSE 'closed'
    END AS status,

    m.responsible_id,
    
    json_build_object(
        'id', u.id,
        'full_name', (u.firstname || ' ' || u.lastname),
        'role', u.role_id
    ) as responsible,

    COALESCE(
        json_agg(
            json_build_object(
                'id', e.id, 
                'name', e.name, 
                'ean', e.ean,
                'status', e.equipment_status_id,
                'department', e.department_id
            )
        ) FILTER (WHERE e.id IS NOT NULL), 
        '[]'
    ) as equipments_summary

FROM maintenances m
LEFT JOIN users u ON u.id = m.responsible_id
LEFT JOIN maintenance_equipments me ON me.maintenance_id = m.id
LEFT JOIN equipments e ON e.id = me.equipment_id

GROUP BY m.id, u.id;