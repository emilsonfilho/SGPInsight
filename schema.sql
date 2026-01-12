CREATE TABLE component_status (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE components (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	name VARCHAR(100) NOT NULL,
	component_status_id UUID NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	discarded_at TIMESTAMP,

	CONSTRAINT fk_component_status
		FOREIGN KEY (component_status_id)
		REFERENCES component_status(id)
);

CREATE TABLE equipment_status (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE roles (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE users (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	firstName VARCHAR(50) NOT NULL,
	lastName VARCHAR(50) NOT NULL,
	email VARCHAR(100) NOT NULL UNIQUE,
	password VARCHAR(100) NOT NULL,
	disabled BOOLEAN NOT NULL DEFAULT FALSE,
	role_id UUID NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

	CONSTRAINT fk_role_id
		FOREIGN KEY (role_id)
		REFERENCES roles(id)
);

CREATE TABLE departments (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	name VARCHAR(100) NOT NULL UNIQUE,
	location VARCHAR(255) NOT NULL,
	responsible_id UUID,

	CONSTRAINT fk_department_responsible
		FOREIGN KEY (responsible_id)
		REFERENCES users(id)
);

CREATE TABLE equipments (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	name VARCHAR(100) NOT NULL,
	ean VARCHAR(50),
	equipment_status_id UUID NOT NULL,
	department_id UUID NOT NULL,

	CONSTRAINT fk_equipment_status
		FOREIGN KEY (equipment_status_id)
		REFERENCES equipment_status(id),

	CONSTRAINT fk_department
		FOREIGN KEY (department_id)
		REFERENCES departments(id)
);

CREATE TABLE maintenances (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	description TEXT NOT NULL,
	responsible_id UUID NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	finished_at TIMESTAMP,

	CONSTRAINT fk_responsible
		FOREIGN KEY (responsible_id)
		REFERENCES users(id)
);

CREATE TABLE instalation_components (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	component_id UUID NOT NULL,
	equipment_id UUID NOT NULL,
	instalation_maintenance_id UUID,
	installed_at TIMESTAMP,
	remotion_maintenance_id UUID,
	removed_at TIMESTAMP,
	observations TEXT,

	CONSTRAINT fk_component
		FOREIGN KEY (component_id)
		REFERENCES components(id),

	CONSTRAINT fk_equipment
		FOREIGN KEY (equipment_id)
		REFERENCES equipments(id),

	CONSTRAINT fk_instalation_maintenance
		FOREIGN KEY (instalation_maintenance_id)
		REFERENCES maintenances(id),

	CONSTRAINT fk_remotion_maintenance
		FOREIGN KEY (remotion_maintenance_id)
		REFERENCES maintenances(id)
);

CREATE TABLE maintenance_equipments (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	maintenance_id UUID NOT NULL,
	equipment_id UUID NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

	UNIQUE (maintenance_id, equipment_id),

	CONSTRAINT fk_maintenance
		FOREIGN KEY (maintenance_id)
		REFERENCES maintenances(id),
		
	CONSTRAINT fk_equipment
		FOREIGN KEY (equipment_id)
		REFERENCES equipments(id)
);

CREATE TABLE equipment_moves (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	equipment_id UUID NOT NULL,
	previously_located_at UUID NOT NULL,
	newly_alocated_at UUID NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

	CONSTRAINT fk_moved_equipment
		FOREIGN KEY (previously_located_at)
		REFERENCES departments(id),

	CONSTRAINT fk_new_location
		FOREIGN KEY (newly_alocated_at)
		REFERENCES departments(id)
);

CREATE TABLE alert_priority (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE alerts (
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	description TEXT NOT NULL,
	origin VARCHAR(50) NOT NULL,
	equipment_id UUID NOT NULL,
	priority_id UUID NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

	CONSTRAINT fk_alert_equipment
		FOREIGN KEY (equipment_id)
		REFERENCES equipments(id),

	CONSTRAINT fk_alert_priority
		FOREIGN KEY (priority_id)
		REFERENCES alert_priority(id)
);
