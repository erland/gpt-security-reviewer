# Scenario: parametrerad JPQL

## Input
`createQuery("select u from User u where u.email = :email").setParameter("email", email)`.

## Expected
Rapportera inte SQL/JPQL injection.
