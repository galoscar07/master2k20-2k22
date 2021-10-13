package Domain;

import java.util.*;

/**
 * 
 */
public abstract class User {

    /**
     * Default constructor
     */
    public User() {
    }

    /**
     * 
     */
    public String firstName;

    /**
     * 
     */
    public String lastName;

    /**
     * 
     */
    private LocalDate bDay;

    /**
     * 
     */
    public Address address;

    /**
     * 
     */
    public Address residence;

    /**
     * 
     */
    private Long CNP;

    /**
     * 
     */
    public String username;

    /**
     * 
     */
    public String password;


    /**
     * @param firstName 
     * @param lastName 
     * @param bDay 
     * @param address 
     * @param residence 
     * @param CNP 
     * @param username 
     * @param password
     */
    public void User(String firstName, String lastName, LocalDate bDay, Address address, Address residence, Long CNP, String username, String password) {
        // TODO implement here
    }

    /**
     * @return
     */
    public Long getCNP() {
        // TODO implement here
        return null;
    }

    /**
     * @return
     */
    public Integer getAge() {
        // TODO implement here
        return null;
    }

    /**
     * @return
     */
    public LocalDate getBDay() {
        // TODO implement here
        return null;
    }

    /**
     * @param firstName 
     * @param lastName 
     * @param address 
     * @param residence
     */
    public void updateAccount(Optional<String> firstName, Optional<String> lastName, Optional<Address> address, Optional<Address> residence) {
        // TODO implement here
    }

}