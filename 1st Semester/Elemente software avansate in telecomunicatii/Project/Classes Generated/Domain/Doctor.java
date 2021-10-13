package Domain;

import java.util.*;

/**
 * 
 */
public class Doctor extends User {

    /**
     * Default constructor
     */
    public Doctor() {
    }

    /**
     * 
     */
    protected UserRepo<Patient> patientList;

    /**
     * 
     */
    public Hospital hospital;



    /**
     * @param firstName 
     * @param lastName 
     * @param bDay 
     * @param address 
     * @param residence 
     * @param CNP 
     * @param hospital
     */
    public void Doctor(String firstName, String lastName, LocalDate bDay, Address address, Address residence, Long CNP, Hospital hospital) {
        // TODO implement here
    }

    /**
     * @param firstName 
     * @param lastName 
     * @param address 
     * @param residence 
     * @param hospital
     */
    public void updateAccount(Optional<String> firstName, Optional<String> lastName, Optional<Address> address, Optional<Address> residence, Optional<Hospital> hospital) {
        // TODO implement here
    }

    /**
     * @param patientID 
     * @return
     */
    public Boolean_TOMOVE enoughDonationsForPatient(Long patientID) {
        // TODO implement here
        return null;
    }

    /**
     * @param move_to 
     * @return
     */
    public TOMOVE trackAllRequestStatuses(repo move_to) {
        // TODO implement here
        return null;
    }

}