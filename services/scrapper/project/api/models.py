import sys
from flask import current_app
from project import db
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql
from sqlalchemy import BigInteger

def unique_join(self, *props, **kwargs):
    if props[0] in [c.entity for c in self._join_entities]:
        return self
    return self.join(*props, **kwargs)

class Building(db.Model):
    __tablename__ = 'building'
    id = db.Column(db.Integer, primary_key=True,
                    unique=True, nullable=False)
    name = db.Column(db.Text, nullable=True)
    address = db.Column(db.Text, nullable=True)
    city = db.Column(db.Text, nullable=True)
    state = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)
    lat = db.Column(db.Float, nullable=True)
    lng = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime(timezone=False),
                             server_default=func.now(), nullable=True)
    Zip = db.Column(db.Text, nullable=True)
    Type = db.Column(db.Text, nullable=True)
    cooperate = db.Column(db.Boolean(), nullable=True)
    summary = db.Column(db.Text, nullable=True)
    company_id = db.Column(db.Integer, nullable=True)
    scrape_city = db.Column(db.Text, nullable=True)
    address_full = db.Column(db.Text, nullable=True)
    media_count = db.Column(db.Integer, nullable=True)
    ts = db.Column(postgresql.TSVECTOR, nullable=True)

    def __init__(self, name, address, city, state, description, lat, lng, Zip, Type, cooperate, summary, company_id, scrape_city, address_full, media_count, ts):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.description = description
        self.lat = lat
        self.lng = lng
        self.Zip = Zip
        self.Type = Type
        self.cooperate = cooperate
        self.summary = summary
        self.company_id = company_id
        self.scrape_city = scrape_city
        self.address_full = address_full
        self.media_count = media_count
        self.ts = ts

class BuildingUnit(db.Model):
    __tablename__ = 'building_unit'
    id = db.Column(db.Integer, primary_key=True,
                    unique=True, nullable=False)
    fk_building_id =db.Column(db.Integer, db.ForeignKey(Building.id),
        nullable=False)
    floor = db.Column(db.Text, nullable=True)
    unit_number = db.Column(db.Text, nullable=True)
    beds = db.Column(db.Integer, nullable=True)
    baths = db.Column(db.Float, nullable=True)
    sqft = db.Column(db.Float, nullable=True)
    price = db.Column(db.Float, nullable=True)
    created_on = db.Column(db.DateTime(timezone=False),
                             server_default=func.now(), nullable=True)
    updated_on = db.Column(db.DateTime(
        timezone=False), server_default=func.now(), onupdate=func.now(), nullable=True)
    scraped_on = db.Column(db.DateTime(
        timezone=False), server_default=func.now(), onupdate=func.now(), nullable=True)                      
    scrape_id = db.Column(db.Integer, nullable=True)
    floorplan = db.Column(db.Text, nullable=True)
    net_price = db.Column(db.Float, nullable=True)
    price_change = db.Column(db.Float, nullable=True)
    source_file = db.Column(db.Text, nullable=True)
    floorplan_fub_id = db.Column(db.Integer, nullable=True)
    available_date = db.Column(db.Text, nullable=True)



    def __init__(self, fk_building_id, floor, unit_number, beds, baths, sqft, price, scrape_id, floorplan, net_price, source_file, price_change, floorplan_fub_id, available_date):
        self.floor = floor
        self.fk_building_id = fk_building_id
        self.unit_number = unit_number
        self.beds = beds
        self.baths = baths
        self.sqft = sqft
        self.price = price
        self.scrape_id = scrape_id
        self.floorplan = floorplan
        self.net_price = net_price
        self.source_file = source_file
        self.price_change = price_change
        self.floorplan_fub_id = floorplan_fub_id
        self.available_date = available_date

class BuildingInfo(db.Model):
    __tablename__ = 'building_info'
    id = db.Column(db.Integer, primary_key=True,
                    unique=True, nullable=False)
    company = db.Column(db.Text, nullable=True)
    website = db.Column(db.Text, nullable=True)
    phone = db.Column(db.Text, nullable=True)
    email = db.Column(db.Text, nullable=True)
    pet_policy = db.Column(db.Text, nullable=True)
    amenities = db.Column(db.JSON, nullable=True)
    neighborhood_name = db.Column(db.Text, nullable=True)
    neighborhood_area = db.Column(db.Text, nullable=True)
    washer_dryer = db.Column(db.Text, nullable=True)
    no_of_units = db.Column(db.Integer, nullable=True)
    balcony = db.Column(db.Text, nullable=True)
    parking = db.Column(db.Text, nullable=True)
    short_term_lease = db.Column(db.Text, nullable=True)
    tour_sunday = db.Column(db.Boolean(), nullable=True)
    cooperation_percentage = db.Column(db.Float, nullable=True)
    concession_months_additional = db.Column(BigInteger, nullable=True)
    scraper_complete = db.Column(db.Boolean(), nullable=True)
    website_reachable = db.Column(db.Boolean(), nullable=True)
    website_needs_ui_navigation = db.Column(db.Boolean(), nullable=True)
    website_data_in_images = db.Column(db.Boolean(), nullable=True)
    data_source = db.Column(db.Text, nullable=True)
    year_built = db.Column(db.Text, nullable=True)
    nearest_grocery_store = db.Column(db.JSON, nullable=True)
    nearest_convenience_store = db.Column(db.JSON, nullable=True)
    nearest_public_transportation = db.Column(db.JSON, nullable=True)
    concession_0_bed = db.Column(db.Float, nullable=True)
    concession_1_bed = db.Column(db.Float, nullable=True)
    concession_2_bed = db.Column(db.Float, nullable=True)
    concession_3_bed = db.Column(db.Float, nullable=True)
    concession_additional = db.Column(db.Float, nullable=True)
    concession_title = db.Column(db.Text, nullable=True)
    leasing_type = db.Column(db.Text, nullable=True)
    concession_update = db.Column(db.DateTime(
        timezone=False), server_default=func.now(), onupdate=func.now(), nullable=True)
    flooring = db.Column(db.Text, nullable=True)
    unit_0_balcony = db.Column(db.Text, nullable=True)
    unit_convert_balcony = db.Column(db.Text, nullable=True)
    unit_1_balcony = db.Column(db.Text, nullable=True)
    unit_2_balcony = db.Column(db.Text, nullable=True)
    unit_3_balcony = db.Column(db.Text, nullable=True)                 
    age = db.Column(db.Integer, nullable=True)
    pool = db.Column(db.Text, nullable=True)
    architect = db.Column(db.JSON, nullable=True)
    aptamigo = db.Column(db.JSON, nullable=True)
    hotspot_features = db.Column(db.JSON, nullable=True)
    hotspot_neighbourhood = db.Column(db.String(250), nullable=True)
    hotspot_description = db.Column(db.String(250), nullable=True)
    hotspot = db.Column(db.JSON, nullable=True)
    concession_source = db.Column(db.Text, nullable=True)
    walk_score = db.Column(db.Integer, nullable=True)
    walk_score_description = db.Column(db.String(250), nullable=True)
    walk_score_updated_date = db.Column(db.DateTime(
        timezone=False), server_default=func.now(), onupdate=func.now(), nullable=True)
    flooring = db.Column(db.Text, nullable=True)
    cooperation_percentage_sent = db.Column(db.Float, nullable=True)
    cooperation_fixed = db.Column(db.Float, nullable=True)
    occupancy_perc = db.Column(db.String(250), nullable=True)
    avg_rent = db.Column(db.String(250), nullable=True)
    avg_eff_rent = db.Column(db.String(250), nullable=True)
    avg_price_per_sqft = db.Column(db.String(250), nullable=True)
    avg_eff_price_per_sqft = db.Column(db.String(250), nullable=True)
    software_system = db.Column(db.String(250), nullable=True)
    min_lease_term = db.Column(db.Float, nullable=True)
    year_renovated = db.Column(db.String(250), nullable=True)
    building_type = db.Column(db.String(250), nullable=True)
    n_units = db.Column(db.Integer, nullable=True)
    n_stories = db.Column(db.Integer, nullable=True)
    regional_supervisor = db.Column(db.String(250), nullable=True)
    onsite_mgr = db.Column(db.String(250), nullable=True)
    section_8 = db.Column(db.Boolean(), nullable=True)
    pets_allowed = db.Column(db.Boolean(), nullable=True)
    dog_allowed = db.Column(db.Boolean(), nullable=True)
    cat_allowed = db.Column(db.Boolean(), nullable=True)
    bird_allowed = db.Column(db.Boolean(), nullable=True)
    pets_details = db.Column(db.JSON, nullable=True)
    approx_price = db.Column(db.JSON, nullable=True)
    cooperation_title = db.Column(db.Text, nullable=True)
    preferred_tour_type = db.Column(db.Integer, nullable=True)
    adjusted_cooperation_percentage = db.Column(db.Float, nullable=True)
    comment = db.Column(db.Text, nullable=True)
    showing_instruction = db.Column(db.Text, nullable=True)

    def __init__(self, company, website, phone, email, pet_policy, amenities, neighborhood_name,
                 neighborhood_area, washer_dryer, no_of_units, balcony, parking, short_term_lease, tour_sunday,
                 cooperation_percentage, concession_months_additional, scraper_complete, website_reachable,
                 website_needs_ui_navigation, website_data_in_images, data_source, year_built, nearest_grocery_store,
                 nearest_convenience_store, nearest_public_transportation, concession_0_bed, concession_1_bed,
                 concession_2_bed, concession_3_bed, concession_additional, concession_title, leasing_type,
                 flooring, unit_0_balcony, unit_convert_balcony, unit_1_balcony, unit_2_balcony,
                 unit_3_balcony, age, pool, architect, aptamigo, hotspot_features, hotspot_neighbourhood,
                 hotspot_description, hotspot, concession_source, walk_score, walk_score_description,
                 cooperation_percentage_sent, cooperation_fixed, occupancy_perc,
                 avg_rent, avg_eff_rent, avg_price_per_sqft, avg_eff_price_per_sqft, software_system,
                 min_lease_term, year_renovated, building_type, n_units, n_stories, regional_supervisor,
                 onsite_mgr, section_8, pets_allowed, dog_allowed, cat_allowed, bird_allowed, pets_details,
                 approx_price, cooperation_title, preferred_tour_type, adjusted_cooperation_percentage,
                 comment, showing_instruction):
        self.company = company
        self.website = website
        self.phone = phone
        self.email = email
        self.pet_policy = pet_policy
        self.amenities = amenities
        self.neighborhood_name = neighborhood_name
        self.neighborhood_area = neighborhood_area
        self.washer_dryer = washer_dryer
        self.no_of_units = no_of_units
        self.balcony = balcony
        self.parking = parking
        self.short_term_lease = short_term_lease
        self.tour_sunday = tour_sunday
        self.cooperation_percentage = cooperation_percentage
        self.concession_months_additional = concession_months_additional
        self.scraper_complete = scraper_complete
        self.website_reachable = website_reachable
        self.website_needs_ui_navigation = website_needs_ui_navigation
        self.website_data_in_images = website_data_in_images
        self.data_source = data_source
        self.year_built = year_built
        self.nearest_grocery_store = nearest_grocery_store
        self.nearest_convenience_store = nearest_convenience_store
        self.nearest_public_transportation = nearest_public_transportation
        self.concession_0_bed = concession_0_bed
        self.concession_1_bed = concession_1_bed
        self.concession_2_bed = concession_2_bed
        self.concession_3_bed = concession_3_bed
        self.concession_additional = concession_additional
        self.concession_title = concession_title
        self.leasing_type = leasing_type
        self.flooring = flooring
        self.unit_0_balcony = unit_0_balcony
        self.unit_convert_balcony = unit_convert_balcony
        self.unit_1_balcony = unit_1_balcony
        self.unit_2_balcony = unit_2_balcony
        self.unit_3_balcony = unit_3_balcony
        self.age = age
        self.pool = pool
        self.architect = architect
        self.aptamigo = aptamigo
        self.hotspot_features = hotspot_features
        self.hotspot_neighbourhood = hotspot_neighbourhood
        self.hotspot_description = hotspot_description
        self.hotspot = hotspot
        self.concession_source = concession_source
        self.walk_score = walk_score
        self.walk_score_description = walk_score_description
        self.cooperation_percentage_sent = cooperation_percentage_sent
        self.cooperation_fixed = cooperation_fixed
        self.occupancy_perc = occupancy_perc
        self.avg_rent = avg_rent
        self.avg_eff_rent = avg_eff_rent
        self.avg_price_per_sqft = avg_price_per_sqft
        self.avg_eff_price_per_sqft = avg_eff_price_per_sqft
        self.software_system = software_system
        self.min_lease_term = min_lease_term
        self.year_renovated = year_renovated
        self.building_type = building_type
        self.n_units = n_units
        self.n_stories = n_stories
        self.regional_supervisor = regional_supervisor
        self.onsite_mgr = onsite_mgr
        self.section_8 = section_8
        self.pets_allowed = pets_allowed
        self.dog_allowed = dog_allowed
        self.cat_allowed = cat_allowed
        self.bird_allowed = bird_allowed
        self.pets_details = pets_details
        self.approx_price = approx_price
        self.cooperation_title = cooperation_title
        self.preferred_tour_type = preferred_tour_type
        self.adjusted_cooperation_percentage = adjusted_cooperation_percentage
        self.comment = comment
        self.showing_instruction = showing_instruction