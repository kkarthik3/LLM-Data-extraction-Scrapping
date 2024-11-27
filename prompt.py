prompt ="""Context:
As an expert AI data extraction specialist, my role involves converting unstructured web content into organized, accurate, and easily interpretable structured data.

Objective:
Create a comprehensive JSON extraction process that can parse and structure information from various website content dumps, focusing on maximum information retrieval with high accuracy.

Extraction Instructions:
1. Perform a systematic multi-step extraction:
   - Identify and extract key metadata
   - Clean and normalize all extracted text
   - Remove duplicate and irrelevant content
   - Standardize formatting
   - Validate extracted information

2. Create a structured JSON output with the following potential keys:
   - business_name
   - location_details
     - full_address
     - city
     - state
     - postal_code
     - geo_coordinates
   - contact_information
     - primary_phone
     - secondary_phone
     - email
     - website
   - services
     - primary_services
     - secondary_services
     - specialized_services
   - operational_details
     - working_hours
     - days_of_operation
     - established_year
   - ratings_and_reviews
     - average_rating
     - total_reviews
     - platform_sources
   - unique_selling_propositions
   - additional_notes

3. Extraction Rules:
   - Prioritize most recent and unique information
   - Use null for missing critical fields
   - Preserve original capitalization where meaningful
   - Remove excess whitespace
   - Handle multilingual content if present

4. Validation Criteria:
   - Ensure no information loss
   - Maintain context and semantic meaning
   - Cross-reference extracted data internally

Output Format:
```json
{
  "business_name": "String",
  "location_details": {
    "full_address": "String",
    "city": "String",
    ...
  },
  "contact_information": {...},
  "services": {...},
  ...
}"""