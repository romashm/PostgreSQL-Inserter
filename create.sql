CREATE TABLE hotelBase (
    ids SERIAL PRIMARY KEY,
    topics VARCHAR(500) NOT NULL,
    timesal VARCHAR(500) NOT NULL,
    hotelName VARCHAR(500) NOT NULL
)

INSERT INTO hotelBase (ids,topics,timesal,hotelName) VALUES 
(1, '[
                {"topic1": "1", "topic2": "2", "topic3": ["3", "4", "5"]},
                {"topic1": "2", "topic2": "3", "topic3": ["6", "8", "9"]},
                {"topic1": "3", "topic2": "4", "topic3": ["12", "8"]},
                {"topic1": "4", "topic2": "5", "topic3": ["122", "18", "19"]},
                {"topic1": "5", "topic2": "6", "topic3": ["61", "81", "91"]}
            ]'::json, '12h', 'hotel1'),
(2, '[
                {"topic1": "11", "topic2": "22", "topic3": ["13", "24", "35"]},
                {"topic1": "21", "topic2": "32", "topic3": ["16", "28", "39"]},
                {"topic1": "31", "topic2": "42", "topic3": ["112", "28"]},
                {"topic1": "41", "topic2": "52", "topic3": ["1122", "218", "319"]},
                {"topic1": "51", "topic2": "62", "topic3": ["161", "281", "391"]}
            ]'::json, '12h', 'hotel2');