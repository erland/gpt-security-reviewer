# Scenario: Java native deserialization

## Input
Extern request-body läses genom `ObjectInputStream.readObject()`.

## Expected
Högprioriterat deserialiseringsfynd om datan är otillförlitlig.
