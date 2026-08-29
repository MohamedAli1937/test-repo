# Emergency Response System

## System Information

The system name is 0-LA Offline AI.
The current software version is 2.4.1.
The deployment environment is offline.
The system is designed for emergency response teams.

## Communication

The primary communication protocol is LoRa.
The backup communication protocol is Wi-Fi Direct.
The maximum recommended LoRa communication range is 8 kilometers in open terrain.

## Power Management

The device contains a 5000 mAh battery.
Normal operating time is approximately 18 hours.
Emergency low-power mode starts when the battery reaches 15%.

## Emergency Procedure

When a critical alert is received:

1. Verify the alert source.
2. Notify the team leader.
3. Establish communication with the field team.
4. Record the incident in the local database.
5. Continue monitoring until the incident is resolved.

## Database

The system uses PostgreSQL with pgvector.
The vector database stores document embeddings.
The embedding model used for this test is all-MiniLM-L12-v2.

## Version History

### Version 2.4.1

Version 2.4.1 introduced LoRa communication and the 5000 mAh battery.

### Version 2.3.0

Version 2.3.0 used Wi-Fi Direct as the primary communication protocol.
The battery capacity was 4000 mAh.

### Version 2.2.0

Version 2.2.0 did not support LoRa.
The system used Wi-Fi Direct only.
