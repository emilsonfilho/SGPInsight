SELECT
    json_build_object(
        'id', e.id,
        'name', e.name,
        'ean', e.ean,
        'status', e.equipment_status_id,
        'department', e.department_id
    ) AS equipment_summary,
    json_build_object(
        'page', %s,
        'per_page', %s,
        'total_records', (SELECT COUNT(*) FROM equipments)
    ) AS pagination,
    json_build_object(
        'movements', (
            SELECT json_agg(
                json_build_object(
                    'id', em.id,
                    'equipment_id', em.equipment_id,
                    'previously_located_at', em.previously_located_at,
                    'newly_alocated_at', em.newly_alocated_at,
                    'date', em.created_at
                )
            )
            FROM equipment_moves em
            WHERE em.equipment_id = e.id
        ),
        'maintenances', (
            SELECT json_agg(
                json_build_object(
                    'id', m.id,
                    'description', m.description,
                    'responsible_id', m.responsible_id,
                    'created_at', m.created_at,
                    'finished_at', m.finished_at
                )
            )
            FROM maintenance_equipments me
            JOIN maintenances m ON m.id = me.maintenance_id
            WHERE me.equipment_id = e.id
        )
    ) AS history_timeline
FROM equipments e
WHERE e.id = %s
OFFSET %s * %s
FETCH NEXT %s ROWS ONLY

SELECT
    json_build_object(
        'id', e.id,
        'name', e.name,
        'ean', e.ean,
        'status', e.equipment_status_id,
        'department', e.department_id
    ) AS equipment_summary,
    json_build_object(
        'page', 1,
        'per_page', 20,
        'total_records', (SELECT COUNT(*) FROM equipments)
    ) AS pagination,
    json_build_object(
        'movements', (
            SELECT json_agg(
                json_build_object(
                    'id', em.id,
                    'equipment_id', em.equipment_id,
                    'previously_located_at', em.previously_located_at,
                    'newly_alocated_at', em.newly_alocated_at,
                    'date', em.created_at
                )
            )
            FROM equipment_moves em
            WHERE em.equipment_id = e.id
        ),
        'maintenances', (
            SELECT json_agg(
                json_build_object(
                    'id', m.id,
                    'description', m.description,
                    'responsible_id', m.responsible_id,
                    'created_at', m.created_at,
                    'finished_at', m.finished_at
                )
            )
            FROM maintenance_equipments me
            JOIN maintenances m ON m.id = me.maintenance_id
            WHERE me.equipment_id = e.id
        )
    ) AS history_timeline
FROM equipments e
WHERE e.id = '052b2e9a-37b9-4c06-96b7-ed9462db861b'
OFFSET 0 * 20
FETCH NEXT 20 ROWS ONLY