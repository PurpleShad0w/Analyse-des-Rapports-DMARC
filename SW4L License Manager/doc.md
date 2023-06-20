# System Workbench for Linux - License Manager Detailled Documentation

This software add-on serves the purpose of managing the licenses of System Workbench in the most efficient and user-friendly way possible. \
It was built using a Bash script meant to regulate the software's launch, a Python script meant to check the validity of the used licenses and a PHP script used to communicate with the SQL database via HTTP requests.

## The Python Script

Upon first execution, this script will prompt the user to provide it with their email, specifically the one the client used to register and purchase their license. Once given, the email will be remembered so that the user does not have to login again before accessing the software. Using the email, the computer's MAC address and the key located in the given license, the script will contact the SQL database to verify all is in order. If it is, then the software will be launched automatically and should do so every other time. If it isn't, then the client will be directed towards registering if the email is lacking in our database, towards checking if they possess the correct license if it is the issue, or be prompted to go renew their license if is expired. There is also another case, where the MAC address of the current computer differs from the one registered. If this is the case, the user will be prompted on whether they wish to replace the registered MAC address with their current one.

## Exit Messages

```expired_license``` - license is past the validation date, user is prompted to renew, software does not launch. \
```incorrect_key``` - key different from registered one, software does not launch. \
```no_date``` - no validation date was found, should not naturally occur, software does not launch. \
```update_acceptance``` - user accepts to replace the MAC address, software launches. \
```update_refusal``` - user does not accept to replace the MAC address, software launches nonetheless. \
```unknown_email``` - email not in database, user is prompted to register, software does not launch. \
```valid_license``` - everything is as intended, software launches. \
```wrong_key``` - key different from registered one, software does not launch.