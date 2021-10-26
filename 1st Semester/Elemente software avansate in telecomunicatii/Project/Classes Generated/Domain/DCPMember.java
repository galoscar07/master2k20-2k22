package Domain;

import java.util.*;

/**
 * 
 */
public class DCPMember extends User {

    /**
     * Default constructor
     */
    public DCPMember() {
    }

    /**
     * 
     */
    protected UserRepo<Donor> donorList;

    /**
     * 
     */
    public DoningCetner doningCenter;



    /**
     * @param firstName 
     * @param lastName 
     * @param bDay 
     * @param address 
     * @param residence 
     * @param CNP 
     * @param doningCenter
     */
    public void DCPMemeber(String firstName, String lastName, LocalDate bDay, Address address, Address residence, Long CNP, DoningCenter doningCenter) {
        // TODO implement here
    }

    /**
     * @param firstName 
     * @param lastName 
     * @param address 
     * @param residence 
     * @param doningCenter
     */
    public void updateAccount(Optional<String> firstName, Optional<String> lastName, Optional<Address> address, Optional<Address> residence, Optional<DoningCenter> doningCenter) {
        // TODO implement here
    }

    /**
     * @param donor 
     * @param appointment
     */
    public void appointDonor(Donor donor, LocalDate appointment) {
        // TODO implement here
    }

    /**
     * @param donor 
     * @return
     */
    public NUJDACAIIBINEAICI updateDonorHistory(Donor donor) {
        // TODO implement here
        return null;
    }

    /**
     * @return
     */
    public NUJDACAIIBINEAICI processRequest() {
        // TODO implement here
        return null;
    }

}