package Domain;

import java.util.*;

/**
 * 
 */
public class Request {

    /**
     * Default constructor
     */
    public Request() {
    }

    /**
     * 
     */
    private Blood blood;

    /**
     * 
     */
    private Integer urgency;

    /**
     * 
     */
    private Hospital hospital;

    /**
     * 
     */
    private Long id;

    /**
     * 
     */
    private static Long idGen = 1;


    /**
     * 
     */
    public void getId() {
        // TODO implement here
    }

    /**
     * @param blood 
     * @param urgency 
     * @param hospital
     */
    public void Request(Blood blood, Integer urgency, Hospital hospital) {
        // TODO implement here
    }

    /**
     * @return
     */
    public Blood getBlood() {
        // TODO implement here
        return null;
    }

    /**
     * @return
     */
    public Integer getUrgency() {
        // TODO implement here
        return null;
    }

    /**
     * @return
     */
    public Hospital getHospital() {
        // TODO implement here
        return null;
    }

}